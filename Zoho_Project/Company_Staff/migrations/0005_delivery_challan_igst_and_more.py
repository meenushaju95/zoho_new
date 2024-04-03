# Generated by Django 5.0 on 2024-04-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0004_reccurring_invoice_reference_recurringinvoice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_challan',
            name='igst',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='delivery_challan',
            name='place_of_supply',
            field=models.CharField(max_length=200, null=True),
        ),
    ]