# Generated by Django 4.0 on 2022-06-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('categories', models.CharField(choices=[('Hiking', 'Hiking'), ('Heritage', 'Heritage'), ('Historical', 'Historical'), ('Nature', 'Nature'), ('Camping', 'Camping'), ('Rafting', 'Rafting'), ('Safari', 'Safari'), ('Trekking', 'Trekking'), ('Sightseeing', 'Sightseeing'), ('Misc.', 'Misc.')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Hiking', 'Hiking'), ('Heritage', 'Heritage'), ('Historical', 'Historical'), ('Nature', 'Nature'), ('Camping', 'Camping'), ('Rafting', 'Rafting'), ('Safari', 'Safari'), ('Trekking', 'Trekking'), ('Sightseeing', 'Sightseeing'), ('Misc.', 'Misc.')], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
