# Generated by Django 4.0.4 on 2022-05-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='decade',
            name='description',
            field=models.TextField(default='No description.'),
        ),
    ]
