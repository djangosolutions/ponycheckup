# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('url', models.URLField()),
                ('no_of_recommendations', models.IntegerField(default=0)),
                ('runs_debug', models.BooleanField()),
                ('supports_https', models.BooleanField()),
                ('heartbleed_vuln', models.BooleanField()),
                ('hsts_header_found', models.BooleanField()),
                ('xframe_header_found', models.BooleanField()),
                ('admin_found', models.BooleanField()),
                ('admin_forces_https', models.NullBooleanField()),
                ('login_found', models.BooleanField()),
                ('login_forces_https', models.NullBooleanField()),
                ('allows_trace', models.BooleanField()),
                ('csrf_cookie_found', models.BooleanField()),
                ('session_cookie_found', models.BooleanField()),
                ('session_cookie_secure', models.NullBooleanField()),
                ('session_cookie_httponly', models.NullBooleanField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]
