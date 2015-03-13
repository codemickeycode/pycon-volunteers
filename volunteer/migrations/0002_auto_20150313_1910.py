# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='committee_id',
            field=models.IntegerField(unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='committeechair',
            name='committee_id',
            field=models.ForeignKey(to_field=b'committee_id', blank=True, to='volunteer.Committee', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='committee_id',
            field=models.ForeignKey(to_field=b'committee_id', blank=True, to='volunteer.Committee', null=True),
            preserve_default=True,
        ),
    ]
