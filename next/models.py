from django.db import models


class Gmail(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=14)

    class Meta:
        verbose_name = 'Данный'
        verbose_name_plural = 'Данные'

    def __str__(self):
        return f'{self.email}'
#
