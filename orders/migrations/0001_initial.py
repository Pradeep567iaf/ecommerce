# Generated by Django 4.1.6 on 2023-02-07 08:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('order_address', models.CharField(max_length=400)),
                ('order_email', models.EmailField(max_length=254)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Shipped', 'Shipped'), ('Awaiting Payment', 'Awaiting Payment'), ('Awaiting Fulfillment', 'Awaiting Fulfillment'), ('Awaiting Shipment', 'Awaiting Shipment')], default='Pending', max_length=25)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
