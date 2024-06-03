# Generated by Django 4.2.11 on 2024-04-16 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prebook',
            name='id_c',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.clients', verbose_name='client_id'),
        ),
        migrations.AlterField(
            model_name='req_info',
            name='id_req',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='book.prebook', verbose_name='req_id'),
        ),
    ]
