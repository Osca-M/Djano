# Generated by Django 2.0.2 on 2018-03-29 20:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('unit_area', models.FloatField()),
                ('unit_perim', models.FloatField()),
                ('district', models.CharField(max_length=50)),
                ('count_field', models.FloatField()),
                ('county_nam', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('owner', models.CharField(db_index=True, max_length=300)),
                ('Title number', models.CharField(max_length=70)),
                ('Area in (Ha)', models.FloatField(max_length=5)),
                ('district', models.CharField(max_length=250)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('A photo of the piece of land', models.ImageField(upload_to='parcels/%Y/%m/%d')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Parcels', to='land.Category')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='land.County')),
            ],
            options={
                'ordering': ('-added',),
            },
        ),
        migrations.AlterIndexTogether(
            name='parcel',
            index_together={('id', 'slug')},
        ),
    ]
