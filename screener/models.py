from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    head_img = models.ImageField()
    description = RichTextUploadingField()
    author = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #if self.slug is None:
        self.slug = slugify(self.title)
        self.save()
        return reverse('view_blog', args = (self.slug,))