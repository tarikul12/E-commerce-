# Generated by Django 5.0 on 2024-01-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_qunatity_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]