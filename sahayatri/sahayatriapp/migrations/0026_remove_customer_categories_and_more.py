# Generated by Django 4.0.5 on 2022-09-10 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahayatriapp', '0025_product_image1_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='municipality',
        ),
        migrations.AddField(
            model_name='customer',
            name='muni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muni1', to='sahayatriapp.municipality'),
        ),
        migrations.AddField(
            model_name='merchant',
            name='muni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muni2', to='sahayatriapp.municipality'),
        ),
        migrations.AddField(
            model_name='product',
            name='budget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bud', to='sahayatriapp.budgetcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district0', to='sahayatriapp.district'),
        ),
        migrations.AddField(
            model_name='product',
            name='entrydate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='muni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muni0', to='sahayatriapp.municipality'),
        ),
        migrations.AddField(
            model_name='product',
            name='offers',
            field=models.CharField(default='N/A', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prov0', to='sahayatriapp.province'),
        ),
        migrations.AddField(
            model_name='product',
            name='valid_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(default='Nepal', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district1', to='sahayatriapp.district'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prov1', to='sahayatriapp.province'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='country',
            field=models.CharField(default='Nepal', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district2', to='sahayatriapp.district'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prov2', to='sahayatriapp.province'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='sahayatriapp.typecategory'),
        ),
    ]
