# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-11 15:59
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0006_auto_20160811_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhoodpage',
            name='draw_neighborhood',
            field=wagtail.wagtailcore.fields.StreamField([('draw', wagtail.wagtailcore.blocks.StructBlock([]))], default=''),
            preserve_default=False,
        ),
    ]
