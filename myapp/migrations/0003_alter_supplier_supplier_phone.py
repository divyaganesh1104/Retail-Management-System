# Generated by Django 4.2.1 on 2023-08-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_customer_custom_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_phone',
            field=models.CharField(max_length=200),
        ),
    ]
