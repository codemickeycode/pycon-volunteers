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
            field=models.IntegerField(null=True, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='committeechair',
            name='committee_id',
            field=models.ForeignKey(null=True, blank=True, to_field='committee_id', to='volunteer.Committee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='committee_id',
            field=models.ForeignKey(null=True, blank=True, to_field='committee_id', to='volunteer.Committee'),
            preserve_default=True,
        ),
    ]
