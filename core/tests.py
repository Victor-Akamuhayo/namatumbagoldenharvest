from io import BytesIO
from tempfile import TemporaryDirectory

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from PIL import Image

from .models import GalleryImage, HomePageHero, ProductCategory, SystemRole, UserRoleAssignment


class RoleModelTests(TestCase):
    def test_sacco_roles_are_defined(self):
        roles = [
            "SUPER_ADMIN",
            "SACCO_MANAGEMENT",
            "FINANCE_OFFICER",
            "LOAN_OFFICER",
            "MEMBERSHIP_OFFICER",
            "AGRICULTURAL_OFFICER",
            "CONTENT_MANAGER",
            "MEMBER",
        ]
        for value in roles:
            self.assertIn(value, [choice[0] for choice in SystemRole.ROLE_CHOICES])

    def test_internal_roles_and_member_role_are_separated(self):
        user = get_user_model().objects.create_user(username="member1", password="secret123")
        member_role = SystemRole.objects.create(name=SystemRole.MEMBER, description="Member role")
        staff_role = SystemRole.objects.create(name=SystemRole.SUPER_ADMIN, description="Super admin role")

        member_assignment = UserRoleAssignment.objects.create(user=user, role=member_role)
        staff_assignment = UserRoleAssignment.objects.create(user=get_user_model().objects.create_user(username="admin1", password="secret123"), role=staff_role)

        self.assertTrue(member_assignment.is_member)
        self.assertFalse(member_assignment.can_view_all_member_data)
        self.assertTrue(staff_assignment.is_internal_staff)
        self.assertTrue(staff_assignment.can_view_all_member_data)


class WebsiteAdminContentTests(TestCase):
    def test_homepage_uses_admin_managed_hero_content(self):
        HomePageHero.objects.create(
            eyebrow='Local growers together',
            title='A new homepage headline',
            tagline='A new message for members',
            feature_title='Our member promise',
            feature_points='Fair loans\nPractical farm advice',
            primary_button_text='Join our SACCO',
            primary_button_url='/membership/',
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A new homepage headline')
        self.assertContains(response, 'A new message for members')
        self.assertContains(response, 'Our member promise')
        self.assertContains(response, 'Fair loans')
        self.assertContains(response, 'Join our SACCO')

    def test_homepage_hero_admin_has_local_image_pickers(self):
        admin_user = get_user_model().objects.create_superuser(
            username='hero-admin',
            email='hero@example.com',
            password='test-password-123',
        )
        self.client.force_login(admin_user)

        response = self.client.get('/admin/core/homepagehero/add/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="background_image"')
        self.assertContains(response, 'name="feature_image"')
        self.assertContains(response, 'type="file"')

    def test_products_page_uses_active_admin_managed_products(self):
        ProductCategory.objects.create(
            name='Test crop',
            image_url='https://example.com/crop.jpg',
            image_alt='Test crop seeds',
            is_active=True,
        )
        ProductCategory.objects.create(
            name='Hidden crop',
            image_url='https://example.com/hidden.jpg',
            image_alt='Hidden crop seeds',
            is_active=False,
        )

        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test crop')
        self.assertNotContains(response, 'Hidden crop')

    def test_admin_route_redirects_anonymous_user_to_login(self):
        response = self.client.get('/admin/')

        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_gallery_admin_add_form_has_a_local_file_picker(self):
        admin_user = get_user_model().objects.create_superuser(
            username='content-admin',
            email='content@example.com',
            password='test-password-123',
        )
        self.client.force_login(admin_user)

        response = self.client.get('/admin/core/galleryimage/add/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="image_file"')
        self.assertContains(response, 'type="file"')

    def test_gallery_admin_saves_a_uploaded_image_file(self):
        admin_user = get_user_model().objects.create_superuser(
            username='gallery-admin',
            email='gallery@example.com',
            password='test-password-123',
        )
        self.client.force_login(admin_user)
        image_buffer = BytesIO()
        Image.new('RGB', (2, 2), color='green').save(image_buffer, format='PNG')

        with TemporaryDirectory() as media_directory:
            with override_settings(MEDIA_ROOT=media_directory):
                response = self.client.post(
                    '/admin/core/galleryimage/add/',
                    {
                        'title': 'Uploaded seedling photo',
                        'category': 'Seedlings',
                        'image_file': SimpleUploadedFile(
                            'seedling.png', image_buffer.getvalue(), content_type='image/png'
                        ),
                        'image_url': '',
                        'caption': 'A test photo',
                    },
                )

                self.assertEqual(response.status_code, 302)
                gallery_image = GalleryImage.objects.get(title='Uploaded seedling photo')
                self.assertTrue(gallery_image.image_file.storage.exists(gallery_image.image_file.name))
