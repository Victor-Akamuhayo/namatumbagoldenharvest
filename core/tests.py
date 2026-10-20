from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import ProductCategory, SystemRole, UserRoleAssignment


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
