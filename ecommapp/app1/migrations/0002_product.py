# Generated by Django 5.0.3 on 2024-03-17 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('description', models.CharField(max_length=2555)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
