# Generated by Django 3.2.8 on 2021-11-06 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0006_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_home_coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='at_home_coffee', to='menu.menu')),
                ('drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drink', to='menu.menu')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='menu.menu')),
                ('merchandise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchandise', to='menu.menu')),
            ],
        ),
    ]