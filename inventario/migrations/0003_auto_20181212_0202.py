# Generated by Django 2.1.2 on 2018-12-12 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_remove_itemiventario_contagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemiventario',
            old_name='contagem_1',
            new_name='contagem_01',
        ),
        migrations.RenameField(
            model_name='itemiventario',
            old_name='contagem_2',
            new_name='contagem_02',
        ),
        migrations.RenameField(
            model_name='itemiventario',
            old_name='contagem_3',
            new_name='contagem_03',
        ),
    ]
