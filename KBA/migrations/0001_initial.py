# Generated by Django 4.0.4 on 2022-06-19 07:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Pitcher', (('P', 'Pitcher'), ('SP', 'Starting Pitcher'), ('RP', 'Relief Pitcher'))), ('Catcher', (('C', 'Catcher'),)), ('Infielder', (('IF', 'Infield'), ('1B', 'First Base'), ('2B', 'Second Base'), ('3B', 'Third Base'), ('SS', 'Shortstop'))), ('Outfielder', (('OF', 'Outfield'), ('LF', 'Left Field'), ('RF', 'Right Field'), ('CF', 'Center Field'))), ('Utility', (('Util', 'Utility'),))], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('year_formed', models.DateField()),
                ('manager', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('no_titles', models.IntegerField()),
                ('updated', models.DateTimeField(default=datetime.datetime(2022, 6, 19, 7, 3, 16, 583563, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(default=datetime.datetime(2022, 6, 19, 7, 3, 16, 584482, tzinfo=utc))),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KBA.team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('bats', models.CharField(choices=[('Right', 'Right'), ('Left', 'Left'), ('Both', 'Both')], max_length=10)),
                ('throws', models.CharField(choices=[('Right', 'Right'), ('Left', 'Left'), ('Both', 'Both')], max_length=10)),
                ('DOB', models.DateField()),
                ('joined', models.DateField()),
                ('experience', models.CharField(choices=[('HS', 'High School'), ('COLL', 'College'), ('D1', 'Division 1'), ('INDY', 'Independent League'), ('MILB', 'Minor League'), ('MLB', 'Major League'), ('PRO', 'A Professional League')], max_length=30, null=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2022, 6, 19, 7, 3, 16, 585117, tzinfo=utc))),
                ('position', models.ManyToManyField(to='KBA.position')),
            ],
        ),
    ]
