
from django.contrib.auth.models import User
from django.db import models
from extention.utils import JalaliDjango
from django.utils import timezone


# Create your models here.





class Post(models.Model):
    Title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(unique=True, verbose_name='آدرس')
    work = models.BooleanField(verbose_name='نمونه کار؟')
    # Category = models.ManyToManyField(Category, related_name='posts')
    Author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='نویسنده')
    Description = models.TextField(verbose_name='متن')
    Image = models.ImageField(upload_to='img', verbose_name='تصویر')
    Publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    Created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    Update = models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در')
    Status = models.BooleanField(default=True, verbose_name='پیش نویس')
    # comments = GenericRelation(Comment)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.Title

    def jpublish(self):
        return JalaliDjango(self.Publish)