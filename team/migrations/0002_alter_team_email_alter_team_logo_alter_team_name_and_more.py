# Generated by Django 4.0.1 on 2022-01-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='website',
            field=models.CharField(max_length=200),
        ),
    ]
