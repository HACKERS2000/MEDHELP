# Generated by Django 3.0.4 on 2020-03-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='number',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
