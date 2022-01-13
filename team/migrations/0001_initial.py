# Generated by Django 4.0.1 on 2022-01-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('bio', models.TextField(max_length=500)),
                ('logo', models.CharField(max_length=500, unique=True)),
                ('website', models.CharField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField(max_length=500)),
                ('players', models.ManyToManyField(blank=True, related_name='teams', to='player.Player')),
            ],
        ),
    ]
