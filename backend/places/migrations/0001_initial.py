# Generated by Django 3.0.4 on 2020-04-02 04:37

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('key', models.TextField(primary_key=True, serialize=False)),
                ('display_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('name', models.TextField()),
                ('key', models.TextField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('bounds', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('photo_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('photo_attribution', models.TextField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('name', models.TextField()),
                ('place_id', models.TextField(primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('user_rating', models.FloatField()),
                ('num_ratings', models.FloatField()),
                ('address', models.TextField()),
                ('email_contact', models.EmailField(blank=True, max_length=254, null=True)),
                ('place_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('image_attribution', models.TextField(blank=True, null=True)),
                ('gift_card_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('takeout_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('donation_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('place_types', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Area')),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_card_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('donation_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('place_id', models.TextField()),
                ('place_name', models.TextField()),
                ('place_rough_location', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('processed', models.BooleanField(default=False)),
                ('matched_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Place')),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedGiftCardLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=1000)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place')),
            ],
        ),
        migrations.CreateModel(
            name='NeighborhoodEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Neighborhood')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place')),
            ],
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='places',
            field=models.ManyToManyField(through='places.NeighborhoodEntry', to='places.Place'),
        ),
        migrations.CreateModel(
            name='EmailSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('processed', models.BooleanField(default=False)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place')),
            ],
        ),
    ]
