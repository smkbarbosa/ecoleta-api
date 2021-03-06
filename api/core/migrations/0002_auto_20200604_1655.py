# Generated by Django 3.0.7 on 2020-06-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='points',
            options={'verbose_name': 'ponto de coleta', 'verbose_name_plural': 'pontos de coleta'},
        ),
        migrations.AddField(
            model_name='points',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='cidade'),
        ),
        migrations.AddField(
            model_name='points',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='imagem'),
        ),
        migrations.AddField(
            model_name='points',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='points',
            name='long',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True, verbose_name='longitude'),
        ),
        migrations.AddField(
            model_name='points',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='nome'),
        ),
        migrations.AddField(
            model_name='points',
            name='number',
            field=models.CharField(max_length=20, null=True, verbose_name='numero'),
        ),
        migrations.AddField(
            model_name='points',
            name='uf',
            field=models.CharField(max_length=2, null=True, verbose_name='estado'),
        ),
    ]
