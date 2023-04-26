# Generated by Django 4.1.7 on 2023-04-26 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_adresselivraison_client_commande_produit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresselivraison',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.client'),
        ),
        migrations.AlterField(
            model_name='adresselivraison',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.commande'),
        ),
        migrations.AlterField(
            model_name='produitcommande',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.commande'),
        ),
        migrations.AlterField(
            model_name='produitcommande',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.produit'),
        ),
    ]
