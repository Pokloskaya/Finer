# Generated by Django 4.0.6 on 2022-10-03 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinerApp', '0004_alter_producto_margen_contribucion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concepto',
            old_name='nombre',
            new_name='nombreConcepto',
        ),
    ]