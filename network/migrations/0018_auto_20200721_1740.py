# Generated by Django 2.2 on 2020-07-21 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_button_device'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='button',
            unique_together={('ip', 'device')},
        ),
    ]
