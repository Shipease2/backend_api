# Generated by Django 5.0 on 2023-12-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipmenttype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]