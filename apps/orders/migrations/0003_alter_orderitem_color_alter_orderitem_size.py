# Generated by Django 4.2 on 2023-04-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem_color_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.CharField(max_length=10, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(max_length=1, null=True, verbose_name='Size'),
        ),
    ]