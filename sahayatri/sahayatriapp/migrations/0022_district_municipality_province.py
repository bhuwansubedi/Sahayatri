# Generated by Django 4.0.5 on 2022-09-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0021_product_days_product_nights'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('province', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('province', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]