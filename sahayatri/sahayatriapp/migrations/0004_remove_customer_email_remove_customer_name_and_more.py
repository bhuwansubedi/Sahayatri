# Generated by Django 4.0 on 2022-06-05 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('sahayatriapp', '0003_customer_type_of_user_merchant_type_of_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='email',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='district',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'), ('Rather not specify', 'Rather not specify')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='municipality',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='province',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='merchant',
            name='age',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='company_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='company_website',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='district',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'), ('Rather not specify', 'Rather not specify')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='municipality',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='pan_no',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='province',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
