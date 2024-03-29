# Generated by Django 4.0.5 on 2022-09-08 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0022_district_municipality_province'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipality',
            name='province',
        ),
        migrations.AlterField(
            model_name='district',
            name='province',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='province', to='sahayatriapp.province'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='district',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='sahayatriapp.district'),
        ),
    ]
