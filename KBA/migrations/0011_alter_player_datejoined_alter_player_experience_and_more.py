# Generated by Django 4.0.5 on 2022-06-23 04:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('KBA', '0010_alter_player_updated_alter_roster_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='dateJoined',
            field=models.IntegerField(choices=[(1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2022, verbose_name='Year Joined'),
        ),
        migrations.AlterField(
            model_name='player',
            name='experience',
            field=models.CharField(blank=True, choices=[('HS', 'High School'), ('COLL', 'College'), ('D1', 'Division 1'), ('INDY', 'Independent League'), ('MILB', 'Minor League'), ('MLB', 'Major League'), ('PRO', 'Other Professional League')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='player',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 4, 18, 22, 332079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='roster',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 4, 18, 22, 331704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 4, 18, 22, 331040, tzinfo=utc)),
        ),
    ]
