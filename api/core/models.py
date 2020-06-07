from django.db import models

# Create your models here.


class Point(models.Model):
    image = models.ImageField('imagem', upload_to='images/', null=True)
    name = models.CharField('nome', max_length=100, null=True)
    lat = models.DecimalField('latitude', max_digits=11, decimal_places=7,null=True)
    long = models.DecimalField('longitude', max_digits=11, decimal_places=7, null=True)
    number = models.CharField('numero', max_length=20, null=True)
    city = models.CharField('cidade',max_length=100, null=True)
    uf = models.CharField('estado', max_length=2, null=True)

    class Meta:
        verbose_name = 'ponto de coleta'
        verbose_name_plural = 'pontos de coleta'

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField('título', max_length=100, default='')
    image = models.ImageField('imagem', upload_to='images/', default='')
    points = models.ManyToManyField('Point', related_name='point')

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'itens'

    def __str__(self):
        return self.title