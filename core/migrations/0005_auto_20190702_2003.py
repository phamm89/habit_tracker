# Generated by Django 2.2.2 on 2019-07-03 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190702_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='date_recorded',
            field=models.DateField(help_text='Enter the date for recording your daily habit'),
        ),
        migrations.AlterUniqueTogether(
            name='dailyrecord',
            unique_together={('habit', 'date_recorded')},
        ),
    ]
