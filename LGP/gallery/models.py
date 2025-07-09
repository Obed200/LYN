
from django.db import models
from django.contrib.auth.models import User
import os

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Lyn Gallery")
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    hero_title = models.CharField(max_length=200, default="Design Your Kitchen with the Experts")
    hero_subtitle = models.CharField(max_length=300, default="$200 Deposit 3D Design & Measurement")
    hero_video = models.FileField(upload_to='videos/', null=True, blank=True)
    contact_email = models.EmailField(default="contact@lyngallery.com")
    contact_phone = models.CharField(max_length=20, default="+1234567890")
    address = models.TextField(default="123 Main St, City, State 12345")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    story = models.TextField(default="Our story...")
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    values = models.TextField(
        default="Innovation:We constantly push the boundaries of design to create unique, innovative solutions for our clients.;"
                "Passion:Our passion for design drives us to deliver exceptional results that exceed expectations.;"
                "Collaboration:We work closely with our clients to ensure their vision becomes reality.;"
                "Excellence:We strive for excellence in every project, no matter how big or small.",
        help_text="Format: Title:Description;Title:Description;..."
    )

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return self.title