# Generated by Django 3.2 on 2023-09-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('super-admin', 'super-admin'), ('sttuf', 'stuff'), ('customer', 'customer')], max_length=50, null=True, verbose_name='type'),
        ),
    ]
