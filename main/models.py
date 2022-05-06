from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=255, verbose_name='Номер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    worker = models.ForeignKey(
        Worker, verbose_name='Работник', on_delete=models.CASCADE, related_name='stores')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'


class Visit(models.Model):
    store = models.ForeignKey(
        Store, verbose_name='Торговая точка', on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=255, verbose_name='Широта')
    longitude = models.FloatField(max_length=255, verbose_name='Долгота')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата/Время')

    def __str__(self):
        return f'{self.store.name}/{self.latitude}, {self.longitude}'

    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'
