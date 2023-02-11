# Generated by Django 4.1.6 on 2023-02-10 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exemplo01', '0004_alter_pessoa_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descricao')),
                ('cid', models.CharField(max_length=20, verbose_name='CID')),
                ('valor', models.FloatField(blank=True, default=None, null=True, verbose_name='Valor')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(default='1990-01-01', verbose_name='Nascimento'),
        ),
        migrations.CreateModel(
            name='procedimento_executado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs', models.CharField(max_length=50, verbose_name='Obs')),
                ('quantidade', models.FloatField(blank=True, default=None, null=True, verbose_name='Quantidade')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exemplo01.pessoa')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exemplo01.procedimento')),
            ],
            options={
                'ordering': ['pessoa', 'procedimento'],
            },
        ),
    ]