# Generated by Django 3.2.9 on 2022-01-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220128_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
