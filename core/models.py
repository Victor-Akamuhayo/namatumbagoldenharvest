from django.conf import settings
from django.db import models


class SystemRole(models.Model):
    SUPER_ADMIN = "SUPER_ADMIN"
    SACCO_MANAGEMENT = "SACCO_MANAGEMENT"
    FINANCE_OFFICER = "FINANCE_OFFICER"
    LOAN_OFFICER = "LOAN_OFFICER"
    MEMBERSHIP_OFFICER = "MEMBERSHIP_OFFICER"
    AGRICULTURAL_OFFICER = "AGRICULTURAL_OFFICER"
    CONTENT_MANAGER = "CONTENT_MANAGER"
    MEMBER = "MEMBER"

    ROLE_CHOICES = [
        (SUPER_ADMIN, "Super Admin"),
        (SACCO_MANAGEMENT, "SACCO Management"),
        (FINANCE_OFFICER, "Finance Officer"),
        (LOAN_OFFICER, "Loan Officer"),
        (MEMBERSHIP_OFFICER, "Membership Officer"),
        (AGRICULTURAL_OFFICER, "Agricultural Officer"),
        (CONTENT_MANAGER, "Content Manager"),
        (MEMBER, "Member"),
    ]

    name = models.CharField(max_length=40, choices=ROLE_CHOICES, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.get_name_display()

    @property
    def is_internal_staff(self):
        return self.name != self.MEMBER

    @property
    def can_view_member_data(self):
        return self.name != self.MEMBER

    class Meta:
        ordering = ['name']


class UserRoleAssignment(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sacco_role')
    role = models.ForeignKey(SystemRole, on_delete=models.PROTECT, related_name='assignments')

    def __str__(self):
        return f"{self.user} - {self.role}"

    @property
    def is_member(self):
        return self.role.name == SystemRole.MEMBER

    @property
    def is_internal_staff(self):
        return self.role.is_internal_staff

    @property
    def can_view_all_member_data(self):
        return self.role.can_view_member_data

    class Meta:
        verbose_name = 'User role assignment'
        verbose_name_plural = 'User role assignments'
        ordering = ['role__name']


class ContactEnquiry(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']


class MembershipApplication(models.Model):
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    district = models.CharField(max_length=100, blank=True)
    sub_county = models.CharField(max_length=100, blank=True)
    village = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    farmer_type = models.CharField(max_length=100, blank=True)
    preferred_contact = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-created_at']


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    body = models.TextField()
    image_url = models.URLField(blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


class GalleryImage(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    image_url = models.URLField()
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['category', 'title']
