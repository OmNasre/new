# signals.py
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Product

@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    # This deletes the image file from the filesystem
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
