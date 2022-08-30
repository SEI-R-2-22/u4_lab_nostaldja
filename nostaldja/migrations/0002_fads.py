# Generated by Django 4.1 on 2022-08-30 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no fad name', max_length=100)),
                ('description', models.CharField(default='no description', max_length=300)),
                ('image_url', models.CharField(max_length=200, null=True)),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decades')),
            ],
        ),
    ]
