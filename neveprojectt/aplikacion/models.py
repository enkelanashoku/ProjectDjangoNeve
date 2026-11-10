
from django.db import models

# Service Model
class Service(models.Model):
    service_slug = models.SlugField(primary_key=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    service_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    service_image = models.ImageField(upload_to="service/")

    def __str__(self):
        return self.service_name


# Contact Model
class Contact(models.Model):
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_surname = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"


# Appointment Model
class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"
        COMPLETED = "completed", "Completed"

    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name="appointments",
    )
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=30, blank=True)
    appointment_at = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_at"]

    def __str__(self):
        return f"{self.customer_name} — {self.service.service_name} ({self.appointment_at:%Y-%m-%d %H:%M})"


# About Model
class About(models.Model):
    welcome_title = models.CharField(max_length=200)
    welcome_description = models.TextField()
    welcome_image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    philosophy_title = models.CharField(max_length=200)
    philosophy_description = models.TextField()

    experience_title = models.CharField(max_length=200)
    experience_description = models.TextField()

    def __str__(self):
        return "About Néve"
class StudioInformation(models.Model):
    studio_name = models.CharField(max_length=200)
    studio_address = models.CharField(max_length=250)
    studio_phone = models.CharField(max_length=30)
    studio_email = models.EmailField()
    instagram_url = models.URLField(blank=True)
    opening_hours = models.TextField()

    def __str__(self):
        return self.studio_name


class Product(models.Model):
    product_slug = models.SlugField(unique=True)
    product_name = models.CharField(max_length=160)
    category = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    usage_instructions = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    image_path = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return self.product_name


class GalleryPost(models.Model):
    class Category(models.TextChoices):
        LASHES_BROWS = "lashes_brows", "Lashes & Brows"
        NAILS = "nails", "Nails"
        HAIR = "hair", "Hair"
        MAKEUP = "makeup", "Makeup"
        SKINCARE = "skincare", "Skin Care"
        STUDIO = "studio", "Studio Rituals"

    title = models.CharField(max_length=140)
    category = models.CharField(max_length=20, choices=Category.choices)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at", "-pk"]
        verbose_name = "Gallery publication"
        verbose_name_plural = "Gallery publications"

    def __str__(self):
        return self.title
