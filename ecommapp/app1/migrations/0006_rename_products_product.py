# Generated by Django 5.0.3 on 2024-03-17 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_products_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]