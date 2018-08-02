# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenVPNLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=128)),
                ('public_ip', models.GenericIPAddressField(verbose_name='IP address')),
                ('vpn_ip', models.GenericIPAddressField(db_index=True, verbose_name='VPN IP address')),
                ('vpn_iface', models.CharField(db_index=True, max_length=8, verbose_name='VPN iface')),
                ('when_connect', models.DateTimeField()),
                ('when_disconnect', models.DateTimeField(null=True)),
                ('bytes_sent', models.PositiveIntegerField(default=None, null=True)),
                ('bytes_received', models.PositiveIntegerField(default=None, null=True)),
            ],
            options={
                'ordering': ['-when_connect'],
                'get_latest_by': 'when_connect',
                'verbose_name': 'OpenVPN log',
            },
        ),
    ]
