# Generated by Django 3.0.5 on 2021-05-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_auto_20210528_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_bill_messages',
            name='Transaction_id',
            field=models.TextField(default='hghgv33'),
        ),
    ]
