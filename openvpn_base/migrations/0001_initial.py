# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('common_name', models.SlugField(max_length=256, blank=True, help_text='Leave blank if you want to let the software assign a common name suitable for your subnet', unique=True, verbose_name='cert name')),
                ('ip', models.GenericIPAddressField(help_text='Leave blank if you want to let the software assign the first available for your network.', null=True, verbose_name='IP address', blank=True)),
                ('company', models.CharField(max_length=256, null=True, verbose_name='company', blank=True)),
                ('name', models.CharField(help_text='It should be Name Surname, or hostname. It has to be unique in company', max_length=128, verbose_name='name')),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
                ('operating_system', models.CharField(default=None, choices=[(b'win', 'Windows'), (b'gnu', 'GNU/Linux')], max_length=32, blank=True, null=True, verbose_name='operating system')),
                ('enabled', models.BooleanField(default=False, verbose_name='enabled')),
                ('cert', models.TextField(default=b'', verbose_name='certificate', blank=True)),
                ('key', models.TextField(default=b'', verbose_name='key', blank=True)),
                ('cert_validity_start', models.DateTimeField(null=True, blank=True)),
                ('cert_validity_end', models.DateTimeField(null=True, blank=True)),
                ('cert_distribution_token', models.CharField(max_length=128, null=True, blank=True)),
                ('cert_distribution_on', models.DateTimeField(null=True, blank=True)),
                ('cert_download_on', models.DateTimeField(null=True, blank=True)),
                ('cert_public_download_on', models.DateTimeField(null=True, blank=True)),
                ('cert_revocation_on', models.DateTimeField(null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('can_access_to', models.ManyToManyField(related_name='can_access_to_rel_+', to='openvpn_base.Client', blank=True)),
            ],
            options={
                'ordering': ('subnet', 'company', 'name'),
            },
        ),
        migrations.CreateModel(
            name='ClientActionsLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=32)),
                ('on', models.DateTimeField(auto_now=True)),
                ('remote_ip', models.GenericIPAddressField(default=b'127.0.0.1')),
                ('note', models.TextField(default=b'', blank=True)),
                ('client', models.ForeignKey(to='openvpn_base.Client')),
            ],
            options={
                'ordering': ['-on'],
                'get_latest_by': 'on',
                'verbose_name': 'action log',
            },
        ),
        migrations.CreateModel(
            name='VPNSubnet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(unique=True, max_length=31, verbose_name='name')),
                ('human_name', models.CharField(unique=True, max_length=128, verbose_name='human name')),
                ('base', models.GenericIPAddressField(unique=True, verbose_name='base')),
                ('bits', models.PositiveSmallIntegerField(verbose_name='bits')),
                ('default_gw', models.GenericIPAddressField(verbose_name='default gateway')),
                ('static_min', models.GenericIPAddressField(verbose_name='first available address')),
                ('static_max', models.GenericIPAddressField(verbose_name='last available address')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('bound_iface', models.CharField(max_length=16, verbose_name='bound interface', blank=True)),
                ('topology', models.CharField(default=b'subnet', max_length=16, verbose_name='topology', choices=[(b'subnet', b'subnet'), (b'net30', b'net30')])),
                ('common_name_template', models.CharField(default=b'%(subnet)s-%(company)s-%(name)s', help_text="Specify a python template string here. Allowed keys are 'name', 'company', 'subnet'", max_length=32, verbose_name='common name template')),
                ('config_server', models.TextField(verbose_name='server configuration', blank=True)),
                ('config_client', models.TextField(verbose_name='client configuration', blank=True)),
            ],
            options={
                'ordering': ['human_name'],
                'abstract': False,
                'verbose_name': 'subnet',
                'verbose_name_plural': 'subnets',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='subnet',
            field=models.ForeignKey(verbose_name='Role', to='openvpn_base.VPNSubnet', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together=set([('company', 'name', 'enabled'), ('ip', 'enabled')]),
        ),
    ]
