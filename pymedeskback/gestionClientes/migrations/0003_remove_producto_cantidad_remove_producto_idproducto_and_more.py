# Generated by Django 4.2.2 on 2023-06-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionClientes', '0002_cliente_remove_pedido_ciudadcliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='idProducto',
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='Valor predeterminado', max_length=100),
        ),
    ]
