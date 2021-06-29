from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    head_img = models.ImageField()
    #description = RichTextField()
    description = RichTextUploadingField()
    author = models.CharField(max_length=50)