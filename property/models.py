from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)
    new_building = models.BooleanField(
        'Новостройка или нет',
        null=True,
        blank=True,
        db_index=True)
    liked_by = models.ManyToManyField(
        User,
        related_name='user_likes',
        null=True,
        blank=True,
        verbose_name='Кто лайкнул:')
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', null=True, blank=True, db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)


    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        related_name='complaints',
        on_delete=models.CASCADE,
        verbose_name='Кто жаловался:')
    apartments = models.ForeignKey(
        Flat,
        related_name='apartaments',
        on_delete=models.CASCADE,
        verbose_name='Квартира на которую жаловались:')
    text_complaint = models.TextField(verbose_name='Текст жалобы:')


class Owner(models.Model):
    owner_name = models.CharField('ФИО владельца:', max_length=200)
    owner_pure_phone = PhoneNumberField(
        'Нормализованный номер владельца:',
        region='RU',
        blank=True)
    flats = models.ManyToManyField(
        Flat,
        related_name='owners',
        verbose_name='Квартиры в собственности:',
        db_index=True)

    def __str__(self):
        return f'{self.owner_name}'
