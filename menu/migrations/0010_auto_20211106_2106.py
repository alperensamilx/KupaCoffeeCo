# Generated by Django 3.2.8 on 2021-11-06 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_delete_drinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='menu.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='menu.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='menu.Flight')),
            ],
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
