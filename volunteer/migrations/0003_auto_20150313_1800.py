# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_committeechairs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Committees',
            new_name='Committee',
        ),
        migrations.RenameModel(
            old_name='CommitteeChairs',
            new_name='CommitteeChair',
        ),
    ]
