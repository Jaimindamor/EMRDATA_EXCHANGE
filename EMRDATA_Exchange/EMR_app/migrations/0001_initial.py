# Generated by Django 5.0.1 on 2024-02-27 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=10, null=True)),
                ('last_name', models.CharField(default='', max_length=10, null=True)),
                ('mobile_number', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(default='', max_length=15, null=True)),
                ('birthdate', models.DateField(blank=True, default='', null=True)),
                ('city', models.CharField(default='', max_length=12, null=True)),
                ('state', models.CharField(default='', max_length=14, null=True)),
                ('pincode', models.CharField(default='', max_length=6, null=True)),
                ('emergency_contant_name', models.CharField(default='', max_length=12, null=True)),
                ('emergency_contant_mobile_number', models.CharField(default='', max_length=10, null=True)),
                ('language', models.CharField(default='', max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=50)),
                ('statusReason', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('type', models.CharField(default='', max_length=50)),
                ('clinic_address', models.CharField(default='', max_length=50)),
                ('notes', models.CharField(default='', max_length=50)),
                ('report', models.FileField(blank=True, null=True, upload_to='')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EMR_app.patient')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
