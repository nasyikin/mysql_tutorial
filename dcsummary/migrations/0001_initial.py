# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rn', models.CharField(max_length=10)),
                ('admit_date', models.DateTimeField()),
                ('discharge_date', models.DateTimeField(null=True, blank=True)),
                ('ward_id', models.CharField(max_length=3)),
                ('physicians', models.TextField()),
                ('chief_complaint', models.TextField()),
                ('main_diagnosis', models.TextField()),
                ('comorbidity', models.TextField()),
                ('procedures', models.TextField()),
                ('medications', models.TextField()),
                ('advice', models.TextField()),
                ('appointment', models.TextField()),
                ('referrer', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('doctor_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
