# Generated by Django 4.1.7 on 2023-05-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
