from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save
from .models import Recipe
import os

@receiver(pre_delete,sender=Recipe)
def delete_images(sender,instance,**kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)


@receiver(pre_save,sender=Recipe)
def message(sender,instance,**kwargs):
    print("An attahment has been saved to the code base.,...")
    print(instance.name)
