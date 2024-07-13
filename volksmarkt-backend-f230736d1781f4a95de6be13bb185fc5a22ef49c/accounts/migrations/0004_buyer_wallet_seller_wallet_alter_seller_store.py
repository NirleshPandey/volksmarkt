# Generated by Django 4.1.1 on 2023-04-17 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stores', '0002_alter_store_category'),
        ('accounts', '0003_seller_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='wallet',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller',
            name='wallet',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seller',
            name='store',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='Stores.store'),
        ),
    ]