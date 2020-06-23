from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Subdivision(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название подразделения')
    supervisor = models.OneToOneField('Emploe', blank=True, null=True, 
                                      on_delete=models.CASCADE, 
                                      related_name='subdivision_supervisor', 
                                      verbose_name='Руководитель')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['title']


class Position(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название должности')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Emploe(MPTTModel):
    name = models.CharField(max_length=64, verbose_name='ФИО')
    date_of_birth = models.DateTimeField(blank=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='photos/%d/%m/%Y', blank=True, verbose_name='Фото')
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name='emploes_position', 
                                 verbose_name='Должность')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, 
                                    blank=True, null=True, related_name='emploes_subdivision',
                                    verbose_name='Подразделение')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, 
                            blank=True, related_name='child',
                            verbose_name='Подчиненный кого')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    class MPTTMeta:
        order_insertion_by = ['name']
