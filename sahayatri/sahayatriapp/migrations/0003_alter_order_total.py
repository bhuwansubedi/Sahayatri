# Generated by Django 4.0.5 on 2022-09-27 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0002_order_refid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
