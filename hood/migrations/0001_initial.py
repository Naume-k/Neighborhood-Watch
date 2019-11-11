# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 11:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Businesses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=150)),
                ('business_description', models.TextField(blank=True)),
                ('contact_person', models.CharField(max_length=150)),
                ('business_email', models.EmailField(max_length=254)),
                ('business_image', models.ImageField(upload_to='media/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_name', models.CharField(max_length=100)),
                ('neighbourhood_location', models.CharField(max_length=100)),
                ('occupants_count', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('1', 'Urgent'), ('2', 'Necessary'), ('3', 'Unessential')], default='None', max_length=50)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('poster_id', models.IntegerField(default=0)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.NeighbourHood')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to='images/')),
                ('userId', models.IntegerField(default=0)),
                ('user_email', models.EmailField(max_length=254)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.NeighbourHood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='hood.Profile'),
        ),
        migrations.AddField(
            model_name='businesses',
            name='business_neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.NeighbourHood'),
        ),
        migrations.AddField(
            model_name='businesses',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
