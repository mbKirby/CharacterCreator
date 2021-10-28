# Generated by Django 3.2.8 on 2021-10-28 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterCreatorDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='currentHitPoints',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='subRaceSelection',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
