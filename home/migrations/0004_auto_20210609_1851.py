# Generated by Django 3.1.1 on 2021-06-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210609_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='application_id',
            field=models.UUIDField(blank=True),
        ),
    ]