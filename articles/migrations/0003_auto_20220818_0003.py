# Generated by Django 2.2.5 on 2022-08-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220817_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='board_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]