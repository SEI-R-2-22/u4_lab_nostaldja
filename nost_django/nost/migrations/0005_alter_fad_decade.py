# Generated by Django 4.0.4 on 2022-05-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nost', '0004_rename_fads_fad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fad',
            name='decade',
            field=models.CharField(max_length=100),
        ),
    ]
