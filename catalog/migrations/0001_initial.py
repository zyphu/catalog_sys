# Generated by Django 3.1.7 on 2021-04-12 18:21

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(help_text='Enter name', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Enter description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(help_text='Enter name', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Enter description')),
                ('acquisition_date', models.CharField(blank=True, default='Unknown', help_text='Please use the following format: <em> YYYY - YYYY </em>', max_length=100)),
                ('creation_date', models.CharField(blank=True, default='Unknown', help_text='Please use the following format: <em> YYYY </em>', max_length=100)),
                ('record_picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('condition_rating', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('5'))], verbose_name='Condition Rating (between 0 and 5)')),
                ('condition_description', models.TextField(blank=True, help_text='Enter condition description')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.manufacturer')),
                ('my_catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.catalog', verbose_name='Catalog')),
            ],
            options={
                'ordering': ['name', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Provenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, default='Unknown', help_text='Please use the following format: <em>YYYY - YYYY<\\em>', max_length=100)),
                ('owner', models.CharField(blank=True, help_text='Enter Owner', max_length=100)),
                ('nation', models.CharField(blank=True, help_text='Enter Nation', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.record')),
            ],
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_label', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(choices=[('char', 'CharField'), ('text', 'TextField'), ('bool', 'Boolean'), ('int', 'Integer'), ('dec', 'Decimal')], default='char', max_length=4)),
                ('cf_char', models.CharField(blank=True, max_length=100)),
                ('cf_text', models.TextField(blank=True)),
                ('cf_bool', models.BooleanField(blank=True, null=True)),
                ('cf_int', models.IntegerField(blank=True, null=True)),
                ('cf_dec', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.record')),
            ],
        ),
    ]