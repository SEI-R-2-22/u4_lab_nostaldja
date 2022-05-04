# Generated by Django 4.0.4 on 2022-05-04 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decade',
            name='start_year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='fad',
            name='decade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decade'),
        ),
    ]