# Generated by Django 4.0.5 on 2022-09-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0033_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg_rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
