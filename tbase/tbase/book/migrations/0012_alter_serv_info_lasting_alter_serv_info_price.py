# Generated by Django 4.2.11 on 2024-05-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_room_info_h_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serv_info',
            name='lasting',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='serv_info',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Стоимость'),
        ),
    ]
