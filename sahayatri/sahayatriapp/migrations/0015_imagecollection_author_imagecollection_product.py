# Generated by Django 4.0.5 on 2022-07-12 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0014_imagecollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecollection',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sahayatriapp.merchant'),
        ),
        migrations.AddField(
            model_name='imagecollection',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img', to='sahayatriapp.product'),
        ),
    ]
