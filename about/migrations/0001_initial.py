# Generated by Django 3.1.5 on 2021-02-15 08:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('Description', ckeditor.fields.RichTextField()),
                ('Image', models.ImageField(upload_to='img', verbose_name='تصویر')),
            ],
        ),
    ]