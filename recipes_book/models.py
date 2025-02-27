from django.db import models
import os
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200,verbose_name='Recipe Of')
    description = models.TextField(verbose_name='Recipe Description')
    image = models.ImageField(verbose_name='Recipe Image',upload_to='recipe/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    # def delete(self, *args, **kwargs):
    #     if self.image and os.path.isfile(self.image.path):
    #         os.remove(self.image.path)
    #     super().delete(*args,**kwargs)
        
    class Meta:
        ordering = ['-created']