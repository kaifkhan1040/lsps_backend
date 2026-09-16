from django.db import models

from apps.core.base import OrderableModel
from apps.core.models import SingletonModel
from django_ckeditor_5.fields import CKEditor5Field


class HomeContent(SingletonModel):
    """Editable 'Welcome Message' block shown on the Home page."""
    welcome_title = models.CharField(max_length=200, default="Welcome to Little Star Public School")
    welcome_text = models.TextField(blank=True)
    welcome_image = models.FileField(upload_to="pages/home/", blank=True, null=True)

    class Meta:
        verbose_name = "Home Page - Welcome Message"
        verbose_name_plural = "Home Page - Welcome Message"

    def __str__(self):
        return "Home Page Welcome Message"

    def save(self, *args, **kwargs):
        # Get the existing database record before saving the new one
        if self.pk:
            try:
                old_instance = type(self).objects.get(pk=self.pk)

                # If a new file is uploaded, delete the old file
                if (
                    old_instance.welcome_image
                    and old_instance.welcome_image != self.welcome_image
                ):
                    old_instance.welcome_image.delete(save=False)

            except type(self).DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file from storage before deleting the database record
        if self.welcome_image:
            self.welcome_image.delete(save=False)

        super().delete(*args, **kwargs)


class ChairmanMessage(SingletonModel):
    """Shown both on Home (preview) and About Us (full)."""
    name = models.CharField(max_length=150, default="Chairman")
    designation = models.CharField(max_length=150, default="Chairman")
    photo = models.ImageField(upload_to="pages/chairman/", blank=True, null=True)
    short_message = models.TextField(help_text="Short excerpt shown on the Home page.")
    full_message = models.TextField(help_text="Full message shown on the About Us page.")
    is_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Chairman's Message"
        verbose_name_plural = "Chairman's Message"

    def __str__(self):
        return "Chairman's Message"

    def save(self, *args, **kwargs):
            # Get the existing database record before saving the new one
            if self.pk:
                try:
                    old_instance = type(self).objects.get(pk=self.pk)
    
                    # If a new file is uploaded, delete the old file
                    if (
                        old_instance.photo
                        and old_instance.photo != self.photo
                    ):
                        old_instance.photo.delete(save=False)
    
                except type(self).DoesNotExist:
                    pass
            super().save(*args, **kwargs)


class PrincipalMessage(SingletonModel):
    name = models.CharField(max_length=150, default="Principal")
    designation = models.CharField(max_length=150, default="Principal")
    photo = models.ImageField(upload_to="pages/principal/", blank=True, null=True)
    short_message = models.TextField(help_text="Short excerpt shown on the Home page.")
    full_message = models.TextField(help_text="Full message shown on the About Us page.")
    is_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Principal's Message"
        verbose_name_plural = "Principal's Message"

    def __str__(self):
        return "Principal's Message"

    def save(self, *args, **kwargs):
            # Get the existing database record before saving the new one
            if self.pk:
                try:
                    old_instance = type(self).objects.get(pk=self.pk)
    
                    # If a new file is uploaded, delete the old file
                    if (
                        old_instance.photo
                        and old_instance.photo != self.photo
                    ):
                        old_instance.photo.delete(save=False)
    
                except type(self).DoesNotExist:
                    pass
            super().save(*args, **kwargs)


class AboutUs(SingletonModel):
    """About Us page: introduction, vision/mission, history, and a
    freeform infrastructure & facilities summary (the detailed,
    itemised facilities live in the `infrastructure` app)."""
    introduction = CKEditor5Field("introduction", config_name="extends")
    vision = CKEditor5Field("vision", config_name="extends")
    mission = CKEditor5Field("mission", config_name="extends")
    # history = models.TextField(blank=True)
    # infrastructure_summary = models.TextField(blank=True)
    banner_image = models.ImageField(upload_to="pages/about/", blank=True, null=True)

    class Meta:
        verbose_name = "About Us Page"
        verbose_name_plural = "About Us Page"

    def __str__(self):
        return "About Us Page"

    def save(self, *args, **kwargs):
            # Get the existing database record before saving the new one
            if self.pk:
                try:
                    old_instance = type(self).objects.get(pk=self.pk)
    
                    # If a new file is uploaded, delete the old file
                    if (
                        old_instance.banner_image
                        and old_instance.banner_image != self.banner_image
                    ):
                        old_instance.banner_image.delete(save=False)
    
                except type(self).DoesNotExist:
                    pass
            super().save(*args, **kwargs)

class History(OrderableModel):
    about_us = models.ForeignKey(AboutUs,on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

class Infrastructure(OrderableModel):
    about_us = models.ForeignKey(AboutUs,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pages/Infrastructure/", blank=True, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
                # Get the existing database record before saving the new one
                if self.pk:
                    try:
                        old_instance = type(self).objects.get(pk=self.pk)
        
                        # If a new file is uploaded, delete the old file
                        if (
                            old_instance.image
                            and old_instance.image != self.image
                        ):
                            old_instance.image.delete(save=False)
        
                    except type(self).DoesNotExist:
                        pass
                super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
            # Delete the file from storage before deleting the database record
            if self.image:
                self.image.delete(save=False)
    
            super().delete(*args, **kwargs)


class SchoolHighlight(OrderableModel):
    """'School Highlights' cards on the Home page."""
    icon = models.CharField(max_length=50, blank=True, help_text="Icon name/class for the frontend.")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class WhyChooseUs(OrderableModel):
    """'Why Choose Little Star Public School' cards."""
    icon = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class QuickLink(OrderableModel):
    """'Quick Links' block on the Home page (e.g. Admissions, Fee
    Structure, Downloads...) — fully admin-managed."""
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, help_text="Internal path (e.g. /admissions) or full URL.")
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
