# Generated by Django 4.0 on 2022-06-05 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0002_customer_merchant_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type_of_user',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='type_of_user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]