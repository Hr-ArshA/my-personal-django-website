from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class About(models.Model):
    Title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='آدرس')
    Description = RichTextField()
    Image = models.ImageField(upload_to='img', verbose_name='تصویر')


    class Meta():
        verbose_name = 'درباه ما'
        verbose_name_plural = 'درباره ما'
