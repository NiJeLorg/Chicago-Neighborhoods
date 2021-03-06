# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-11 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('neighborhoods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighborhoodPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='Updated On')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='neighborhoods.neighborhoodCHI')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NeighborhoodPages',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
