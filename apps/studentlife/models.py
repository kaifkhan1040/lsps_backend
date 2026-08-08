from django.db import models

from apps.core.base import OrderableModel, TimeStampedModel


class ActivityCategory(OrderableModel):
    """Sports, Dance & Music, Art & Craft, Public Speaking, Community
    Helper Activities, Educational Trips & Excursions, School Events &
    Celebrations -- admin can add/edit/delete categories freely."""
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class ActivityPost(TimeStampedModel):
    """An individual activity/event write-up under a category, with
    photos (inline) and an optional video."""
    category = models.ForeignKey(
        ActivityCategory, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    cover_image = models.ImageField(upload_to="studentlife/covers/", blank=True, null=True)
    video_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return self.title


class ActivityPhoto(models.Model):
    post = models.ForeignKey(ActivityPost, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="studentlife/photos/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Photo for {self.post.title}"
