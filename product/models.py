from django.db import models


class Product(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    size = models.IntegerField(default=38, verbose_name='Размер')
    color = models.CharField(max_length=256, verbose_name='Цвет')
    image = models.ImageField(upload_to='product_images', verbose_name='Фото')
    update = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title}'
