from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from .address import Address


from taggit.managers import TaggableManager

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100, null= True, blank=True)
    slug = models.SlugField(unique = True, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
        
    class Meta:
        verbose_name_plural = "Author"


class Sermon(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 255, null= True, blank=True)
    slug = models.SlugField(unique = True, blank=True, null=True)
    img = models.ImageField(upload_to='sermon',
    default='', null = True, blank= True
    )
    audio = models.FileField(upload_to= 'audio', null= True, blank=True)


    like = models.ManyToManyField(Address, related_name= 'likes', blank=True)
    like_count = models.BigIntegerField(default = 0, null= True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return f"{self.author.name} - {self.title}"
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Sermon"

