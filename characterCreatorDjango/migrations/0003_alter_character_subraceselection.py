# Generated by Django 3.2.8 on 2021-10-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterCreatorDjango', '0002_auto_20211028_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='subRaceSelection',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
