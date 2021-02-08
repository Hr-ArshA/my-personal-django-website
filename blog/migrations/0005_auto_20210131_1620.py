# Generated by Django 3.1.5 on 2021-01-31 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210130_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['Position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterField(
            model_name='category',
            name='Position',
            field=models.IntegerField(verbose_name='پوزیشن'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Status',
            field=models.BooleanField(default=True, verbose_name='نمایش داده شود؟'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Status',
            field=models.BooleanField(default=True, verbose_name='نمایش داده شود؟'),
        ),
    ]