# Generated by Django 5.1.1 on 2024-09-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_inventoryusage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiptionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=300)),
                ('contact_number', models.IntegerField(max_length=11)),
            ],
        ),
    ]
