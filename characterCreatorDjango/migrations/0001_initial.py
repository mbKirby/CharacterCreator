# Generated by Django 3.2.8 on 2021-10-13 22:20

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
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('characterLevel', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('hair', models.CharField(max_length=100)),
                ('eye', models.CharField(max_length=100)),
                ('skinColor', models.CharField(max_length=100)),
                ('backstory', models.CharField(max_length=100)),
                ('armorClass', models.PositiveIntegerField()),
                ('hitPoints', models.PositiveIntegerField()),
                ('Speed', models.PositiveIntegerField()),
                ('passivePerception', models.PositiveIntegerField()),
                ('darkVision', models.PositiveIntegerField()),
                ('background', models.CharField(max_length=100)),
                ('raceSelection', models.CharField(max_length=100)),
                ('subClassSelection', models.CharField(max_length=100)),
                ('classSelection', models.CharField(max_length=100)),
                ('subRaceSelection', models.CharField(max_length=100)),
                ('alignmentSelection', models.CharField(max_length=100)),
                ('chosenProficiencies', models.CharField(max_length=100)),
                ('cha', models.PositiveIntegerField()),
                ('con', models.PositiveIntegerField()),
                ('dex', models.PositiveIntegerField()),
                ('int', models.PositiveIntegerField()),
                ('str', models.PositiveIntegerField()),
                ('wis', models.PositiveIntegerField()),
                ('languageToolProficienciesSelection', models.CharField(max_length=100)),
                ('cantripsSelection', models.CharField(max_length=100)),
                ('equipment', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
