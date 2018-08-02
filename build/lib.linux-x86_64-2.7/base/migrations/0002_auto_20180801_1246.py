# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='can_access_to',
            field=models.ManyToManyField(related_name='can_access_to_rel_+', to='base.Client', blank=True),
        ),
    ]
