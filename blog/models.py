from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Main_model(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(models.TextField())
    image = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)