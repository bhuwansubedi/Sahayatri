# Generated by Django 4.0.5 on 2022-09-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0019_itnerary_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mapurl',
            field=models.URLField(null=True),
        ),
    ]
