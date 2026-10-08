from django.contrib import admin

from .models import ContactEnquiry, GalleryImage, MembershipApplication, NewsArticle, SystemRole, UserRoleAssignment


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject')
    list_filter = ('created_at',)


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'district', 'farmer_type', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'district', 'farmer_type')
    list_filter = ('created_at', 'district')


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'summary', 'body')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_url')
    search_fields = ('title', 'category', 'caption')


@admin.register(SystemRole)
class SystemRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(UserRoleAssignment)
class UserRoleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role__name')
    list_filter = ('role',)
