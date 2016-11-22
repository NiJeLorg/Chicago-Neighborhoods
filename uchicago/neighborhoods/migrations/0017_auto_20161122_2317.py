# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 23:17
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0016_auto_20161109_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='chicagoneighborhoods',
            name='final_project',
            field=wagtail.wagtailcore.fields.StreamField([('draw', wagtail.wagtailcore.blocks.StructBlock([(b'drawnNeighborhood', wagtail.wagtailcore.blocks.TextBlock())])), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='heading')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock())], default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urbandesign',
            name='final_project',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='heading')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock()), ('draw', wagtail.wagtailcore.blocks.StructBlock([(b'drawnNeighborhood', wagtail.wagtailcore.blocks.TextBlock())]))], default=''),
            preserve_default=False,
        ),
    ]
