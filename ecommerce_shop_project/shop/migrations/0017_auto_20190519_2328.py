# Generated by Django 2.1.7 on 2019-05-19 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_percent', models.PositiveIntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='original_price',
        ),
        migrations.AddField(
            model_name='productdiscount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='discounts', to='shop.Product'),
        ),
    ]
