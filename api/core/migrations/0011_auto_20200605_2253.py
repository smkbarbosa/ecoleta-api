# Generated by Django 3.0.7 on 2020-06-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200605_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='imagem'),
        ),
    ]
