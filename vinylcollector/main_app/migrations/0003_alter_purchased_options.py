# Generated by Django 5.0.1 on 2024-02-06 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_purchased'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchased',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Purchased'},
        ),
    ]