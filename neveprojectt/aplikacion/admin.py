from django.contrib import admin
from .models import Service, Contact, Appointment, About, GalleryPost, Product, StudioInformation


@admin.register(GalleryPost)
class GalleryPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'is_published', 'created_at')
    list_filter = ('category', 'is_featured', 'is_published')
    search_fields = ('title', 'caption')
    list_editable = ('is_featured', 'is_published')
    fieldsets = (
        (None, {'fields': ('title', 'category', 'caption', 'image')}),
        ('Publishing', {'fields': ('is_featured', 'is_published')}),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('product_name', 'product_slug', 'description')
    prepopulated_fields = {'product_slug': ('product_name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_slug', 'service_name', 'service_price')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_surname', 'contact_email')
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service', 'appointment_at', 'status')
    list_filter = ('status', 'appointment_at')
    search_fields = ('customer_name', 'customer_email', 'service__service_name')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('welcome_title', 'philosophy_title', 'experience_title')
@admin.register(StudioInformation)
class StudioInformationAdmin(admin.ModelAdmin):
    list_display = (
        'studio_name',
        'studio_phone',
        'studio_email',
        'instagram_url',
        'opening_hours',
        'studio_address',
    )
