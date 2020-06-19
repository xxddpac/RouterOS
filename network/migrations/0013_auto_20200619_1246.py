# Generated by Django 2.2 on 2020-06-19 04:46

import cidrfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_button_ip_export'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='ip',
            field=cidrfield.models.IPNetworkField(null=True, verbose_name='路由地址'),
        ),
        migrations.AlterField(
            model_name='button',
            name='ip_export',
            field=models.CharField(choices=[('l2tp-xg', '香港出口'), ('l2tp-hd', '海底光缆出口'), ('l2tp-dx', '电信精品出口'), ('l2tp-al', '阿里云出口'), ('l2tp-tx', '腾讯云出口')], default='', max_length=10, verbose_name='ip出口'),
        ),
    ]
