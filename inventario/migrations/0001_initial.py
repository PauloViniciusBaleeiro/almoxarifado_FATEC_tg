# Generated by Django 2.1.2 on 2018-12-12 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='data de realização')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'inventario',
                'verbose_name_plural': 'inventarios',
            },
        ),
        migrations.CreateModel(
            name='ItemIventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('contagem', models.PositiveIntegerField(blank=True, null=True)),
                ('contagem_1', models.PositiveIntegerField(blank=True, null=True)),
                ('contagem_2', models.PositiveIntegerField(blank=True, null=True)),
                ('contagem_3', models.PositiveIntegerField(blank=True, null=True)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Inventario')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Material')),
            ],
            options={
                'verbose_name': 'item de inventario',
                'verbose_name_plural': 'itens de inventário',
            },
        ),
        migrations.AlterUniqueTogether(
            name='itemiventario',
            unique_together={('inventario', 'material')},
        ),
    ]
