# Generated by Django 5.0 on 2024-04-16 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0008_alter_delivery_challan_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_challan',
            name='invoice_convert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.invoice'),
        ),
        migrations.AddField(
            model_name='delivery_challan',
            name='rec_invoice_convert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.recurringinvoice'),
        ),
    ]
