# Generated by Django 4.2.11 on 2024-05-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
