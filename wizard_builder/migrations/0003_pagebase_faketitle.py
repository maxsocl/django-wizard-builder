# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-10 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0002_remove_formquestion_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagebase',
            name='faketitle',
            field=models.TextField(blank=True),
        ),
    ]
