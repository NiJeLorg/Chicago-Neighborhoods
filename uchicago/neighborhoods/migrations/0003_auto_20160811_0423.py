# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-11 04:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0002_neighborhoodpage_neighborhoodpages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NeighborhoodPages',
            new_name='HomePage',
        ),
    ]
