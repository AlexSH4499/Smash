# Generated by Django 2.1.2 on 2018-12-22 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tierlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tier',
            name='fighters',
            field=models.ManyToManyField(to='tierlist.Fighter'),
        ),
    ]