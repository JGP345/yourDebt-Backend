# Generated by Django 4.0.4 on 2022-05-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourdebt', '0002_debt_amount_owed_debt_int_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='mortgage',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
