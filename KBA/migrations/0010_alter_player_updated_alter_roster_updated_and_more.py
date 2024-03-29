# Generated by Django 4.0.5 on 2022-06-23 04:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('KBA', '0009_remove_player_joined_remove_player_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 4, 11, 46, 388945, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roster',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 4, 11, 46, 388555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 4, 11, 46, 387900, tzinfo=utc)),
        ),
    ]
