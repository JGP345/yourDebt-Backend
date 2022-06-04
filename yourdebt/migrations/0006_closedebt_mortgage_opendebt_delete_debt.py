# Generated by Django 4.0.4 on 2022-05-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourdebt', '0005_debt_extra_principal_debt_min_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloseDebt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_name', models.CharField(max_length=150)),
                ('amount_owed', models.IntegerField()),
                ('int_rate', models.IntegerField()),
                ('min_payment', models.IntegerField()),
                ('extra_principal', models.IntegerField()),
                ('time_topay', models.IntegerField()),
                ('term', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mortgage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mortgage_name', models.CharField(max_length=150)),
                ('purchase_price', models.IntegerField()),
                ('down_payment', models.IntegerField()),
                ('int_rate', models.IntegerField()),
                ('property_tax', models.IntegerField()),
                ('property_insurance', models.IntegerField()),
                ('PMI', models.IntegerField()),
                ('first_month', models.IntegerField()),
                ('first_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OpenDebt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_name', models.CharField(max_length=150)),
                ('amount_owed', models.IntegerField()),
                ('int_rate', models.IntegerField()),
                ('min_payment', models.IntegerField()),
                ('extra_principal', models.IntegerField()),
                ('time_topay', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Debt',
        ),
    ]
