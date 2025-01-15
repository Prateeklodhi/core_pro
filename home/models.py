from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        ordering = ['name']