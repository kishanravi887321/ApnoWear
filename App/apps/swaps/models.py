from django.db import models
from django.conf import settings
from apps.items.models import Item

class Purchase(models.Model):
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed")],
        default="Pending"
    )
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.email} bought {self.item.name}"
