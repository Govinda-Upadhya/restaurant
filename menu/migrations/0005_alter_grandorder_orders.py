# Generated by Django 5.0.4 on 2024-04-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_rename_sum_orderdetail_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grandorder',
            name='orders',
            field=models.ManyToManyField(blank=True, to='menu.orderdetail'),
        ),
    ]
