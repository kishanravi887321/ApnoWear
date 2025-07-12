
from django.conf import settings
from django.db import models

class Item(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,           
        on_delete=models.CASCADE,
        related_name='items'
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
