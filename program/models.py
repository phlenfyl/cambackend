from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from .address import Address


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length = 255, null= True, blank=True)
    slug = models.SlugField(unique = True, blank=True, null=True)
    desc = RichTextField(null= True, blank=True)
    img = models.ImageField(upload_to='program',
    default='', null = True, blank= True
    )
    video = EmbedVideoField(null= True, blank=True)


    like = models.ManyToManyField(Address, related_name= 'likes', blank=True)
    like_count = models.BigIntegerField(default = 0, null= True, blank=True)

    speicalprogram= models.BooleanField(null= True, blank=True)
    deliverance = models.BooleanField(null= True, blank=True)
    counseling = models.BooleanField(null= True, blank=True)

    display = models.BooleanField(null= True, blank=True)
    
    date = models.CharField(max_length = 50, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ('', kwargs=(self.slug))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Program"

class ProgramNum(models.Model):
    name = models.ForeignKey(Program, on_delete = models.CASCADE, related_name = 'pag')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "ProgramNum"

# class SpeialProgram(models.Model):
#     title = models.CharField(max_length = 255, null= True, blank=True)
#     slug = models.SlugField(unique = True, blank=True, null=True)
#     desc = RichTextField(null= True, blank=True)
#     img = models.ImageField(upload_to='special',
#     default='', null = True, blank= True
#     )
#     video = EmbedVideoField(null= True, blank=True)


#     like = models.ManyToManyField(Address, related_name= 'likes', blank=True)
#     like_count = models.BigIntegerField(default = 0, null= True, blank=True)
    
    
#     date = models.CharField(max_length = 50, null= True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


#     tags = TaggableManager(blank=True)

#     def __str__(self):
#         return self.title
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         return super().save(*args, **kwargs)
    
#     class Meta:
#         verbose_name_plural = "Special Program"
