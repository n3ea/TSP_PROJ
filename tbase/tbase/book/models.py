from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Room_Info(models.Model):
    title = models.CharField('Название услуги', max_length=50)
    places = models.IntegerField('Количество мест', null=True, blank=True)
    price = models.CharField('Суточная стоимость', max_length=50, null=True, blank=True)
    h_ph = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title

class Serv_Info(models.Model):
    serv_name = models.CharField('Наименование услуги', max_length=250)
    lasting = models.CharField('Длительность', max_length=50, null=True, blank=True)
    price = models.CharField('Стоимость', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.serv_name

class Clients(models.Model):
    id_cl = models.AutoField('ID клиента', primary_key=True)
    fio = models.CharField('ФИО клиента', max_length=250)
    login = models.CharField('Логин клиента', max_length=250, unique=True, default='a')
    password = models.CharField('Пароль клиента', max_length=50)
    tel_n = models.CharField('Телефон клиента', max_length=250)
    e_mail = models.CharField('Почта клиента', max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'id: {self.id_cl}'

class Prebook(models.Model):
    CHOICES = (('1', 'Ожидает подтверждения'), ('2', 'Подтверждено'), ('3', 'Отменено'))
    id_req = models.AutoField('ID заявки брони', primary_key=True)
    id_c = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='client_id')
    room_nums = models.ManyToManyField(Room_Info)
    serv_n = models.ManyToManyField(Serv_Info)
    b_start = models.DateField('Дата заезда', null=True)
    b_end = models.DateField('Дата выезда', null=True)
    stat = models.CharField('Статус брони', max_length=50, choices=CHOICES, default='1')

    def __str__(self):
        return f'id: {self.id_req}'


# class Req_Info(models.Model):
#     CHOISES = (('1', 'Ожидает подтверждения'), ('2', 'Подтверждено'), ('3','Отменено'))
#     id_req = models.OneToOneField(Prebook, on_delete=models.CASCADE, primary_key=True, verbose_name = 'req_id' )       #если удаляется запись в данной табл, то удаляется и в пребуке
#     stat = models.CharField('Статус брони', max_length=50, choices=CHOISES, default='Ожидает подтверждения')
#
#
#     def __str__(self):
#         return f'{self.id_req}'

