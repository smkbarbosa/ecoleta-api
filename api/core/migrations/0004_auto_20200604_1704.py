# Generated by Django 3.0.7 on 2020-06-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='imagem'),
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='título'),
        ),
    ]
