# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenVPNLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common_name', models.CharField(max_length=128)),
                ('public_ip', models.GenericIPAddressField(verbose_name='IP address')),
                ('vpn_ip', models.GenericIPAddressField(verbose_name='VPN IP address', db_index=True)),
                ('vpn_iface', models.CharField(max_length=8, verbose_name='VPN iface', db_index=True)),
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
