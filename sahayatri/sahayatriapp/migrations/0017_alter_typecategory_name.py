# Generated by Django 4.0 on 2022-07-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0016_alter_imagecollection_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typecategory',
            name='name',
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]