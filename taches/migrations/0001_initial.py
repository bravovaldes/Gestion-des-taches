# Generated by Django 4.2.1 on 2023-06-05 17:57

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
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('statut', models.CharField(max_length=50)),
                ('priorite', models.CharField(max_length=50)),
                ('debut', models.DateTimeField(auto_now=True)),
                ('fin', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(max_length=30)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taches.categorie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
