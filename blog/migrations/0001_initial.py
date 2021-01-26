# Generated by Django 3.1.5 on 2021-01-26 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس')),
                ('work', models.BooleanField(verbose_name='نمونه کار؟')),
                ('Description', models.TextField(verbose_name='متن')),
                ('Image', models.ImageField(upload_to='img', verbose_name='تصویر')),
                ('Publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('Created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('Update', models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در')),
                ('Status', models.BooleanField(default=True, verbose_name='پیش نویس')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
    ]
