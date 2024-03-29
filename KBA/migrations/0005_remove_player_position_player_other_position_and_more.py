# Generated by Django 4.0.5 on 2022-06-23 03:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('KBA', '0004_remove_player_position_player_position_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
        migrations.AddField(
            model_name='player',
            name='other_position',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Pitcher', (('P', 'Pitcher'), ('SP', 'Starting Pitcher'), ('RP', 'Relief Pitcher'))), ('Catcher', (('C', 'Catcher'),)), ('Infielder', (('IF', 'Infield'), ('1B', 'First Base'), ('2B', 'Second Base'), ('3B', 'Third Base'), ('SS', 'Shortstop'))), ('Outfielder', (('OF', 'Outfield'), ('LF', 'Left Field'), ('RF', 'Right Field'), ('CF', 'Center Field'))), ('Utility', (('Util', 'Utility'),))], max_length=44, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='primary_position',
            field=models.CharField(choices=[('Pitcher', (('P', 'Pitcher'), ('SP', 'Starting Pitcher'), ('RP', 'Relief Pitcher'))), ('Catcher', (('C', 'Catcher'),)), ('Infielder', (('IF', 'Infield'), ('1B', 'First Base'), ('2B', 'Second Base'), ('3B', 'Third Base'), ('SS', 'Shortstop'))), ('Outfielder', (('OF', 'Outfield'), ('LF', 'Left Field'), ('RF', 'Right Field'), ('CF', 'Center Field'))), ('Utility', (('Util', 'Utility'),))], default='unselected', max_length=30),
        ),
        migrations.AlterField(
            model_name='player',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 3, 23, 51, 655256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roster',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 3, 23, 51, 654727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 3, 23, 51, 653708, tzinfo=utc)),
        ),
    ]
