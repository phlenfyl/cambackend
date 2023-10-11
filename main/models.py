from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
# Create your models here.

class WeekService(models.Model):
    name = models.CharField(max_length = 255, null= True, blank=True)
    slug = models.SlugField(unique = True, blank=True, null=True)
    img = models.ImageField(upload_to='weekly',
    default='', null = True, blank= True
    )
    image = CloudinaryField('Image', overwrite= True, format= 'jpg', blank=True, null=True)
    time = models.CharField(max_length=50,null= True, blank=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Week Service"
