# Generated by Django 2.1.7 on 2019-05-13 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20190513_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdiscount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='discounts', to='shop.Product'),
        ),
    ]
