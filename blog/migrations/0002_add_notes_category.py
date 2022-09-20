# Generated by Django 3.2.13 on 2022-09-20 16:30

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='Other', max_length=50)),
                ('category_pic', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(default='Other', on_delete=django.db.models.deletion.PROTECT, related_name='post_category', to='blog.category'),
        ),
    ]
