from django.contrib import admin

from .models import ContactEnquiry, GalleryImage, HomePageHero, MembershipApplication, NewsArticle, ProductCategory, SystemRole, UserRoleAssignment


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
    fields = ('title', 'summary', 'body', 'image_file', 'image_url', 'published_at')
    readonly_fields = ('published_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_file')
    search_fields = ('title', 'category', 'caption')
    fields = ('title', 'category', 'image_file', 'image_url', 'caption')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order', 'is_active')
    list_editable = ('display_order', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    ordering = ('display_order', 'name')
    fields = ('name', 'image_file', 'image_url', 'image_alt', 'image_source', 'description', 'display_order', 'is_active')


@admin.register(HomePageHero)
class HomePageHeroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero content', {'fields': ('eyebrow', 'title', 'subtitle', 'tagline', 'background_image')}),
        ('Buttons', {'fields': ('primary_button_text', 'primary_button_url', 'secondary_button_text', 'secondary_button_url')}),
        ('Feature panel', {'fields': ('feature_image', 'feature_image_alt', 'feature_title', 'feature_points')}),
        ('Statistics', {'fields': (
            ('stat_one_value', 'stat_one_label'),
            ('stat_two_value', 'stat_two_label'),
            ('stat_three_value', 'stat_three_label'),
        )}),
    )

    def has_add_permission(self, request):
        return not HomePageHero.objects.exists() and super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if not HomePageHero.objects.exists():
            from django.shortcuts import redirect
            return redirect('admin:core_homepagehero_add')
        return super().changelist_view(request, extra_context)


@admin.register(SystemRole)
class SystemRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(UserRoleAssignment)
class UserRoleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role__name')
    list_filter = ('role',)
