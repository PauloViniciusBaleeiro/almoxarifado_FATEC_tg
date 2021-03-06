# Generated by Django 2.1.2 on 2018-12-12 02:04

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
            name='Devolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Devolução',
                'verbose_name_plural': 'Devoluções',
            },
        ),
        migrations.CreateModel(
            name='ItemDevolucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=30)),
                ('quantidade', models.FloatField(default=0)),
                ('devolução', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movimento.Devolucao')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Material')),
            ],
            options={
                'verbose_name': 'Item - Devoluçaõ',
                'verbose_name_plural': 'Itens - devoluções',
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_do_movimento', models.DateField(auto_now=True)),
                ('tipo_de_movimento', models.CharField(choices=[('E', 'entrada'), ('S', 'saída'), ('P', 'perda'), ('A', 'avaria')], max_length=1)),
                ('usuário', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movimento',
                'verbose_name_plural': 'Movimentos',
            },
        ),
        migrations.CreateModel(
            name='MovimentoMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=20)),
                ('quatidade', models.FloatField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Material')),
                ('movimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movimento.Movimento')),
            ],
            options={
                'verbose_name': 'Movimento - material',
                'verbose_name_plural': 'Movimento-material',
            },
        ),
        migrations.CreateModel(
            name='Requisicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('situação', models.CharField(choices=[('A', 'ABERTO'), ('PA', 'PARCIALMENTE ATENDIDA'), ('F', 'FECHADA')], max_length=2)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'requisição',
                'verbose_name_plural': 'requisições',
            },
        ),
        migrations.CreateModel(
            name='RequisicaoMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviço', models.CharField(choices=[('1', 'Desjejum'), ('2', 'Almoço'), ('3', 'Café da tarde'), ('4', 'Jantar'), ('5', 'Lanche noturno')], help_text='almoço, jantar, desejum...', max_length=30)),
                ('quantidade', models.FloatField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Material')),
                ('requisicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movimento.Requisicao')),
            ],
            options={
                'verbose_name_plural': 'requisições - materiais',
            },
        ),
        migrations.AlterUniqueTogether(
            name='requisicaomaterial',
            unique_together={('requisicao', 'material')},
        ),
        migrations.AlterUniqueTogether(
            name='movimentomaterial',
            unique_together={('movimento', 'material')},
        ),
        migrations.AlterUniqueTogether(
            name='itemdevolucao',
            unique_together={('devolução', 'material')},
        ),
    ]
