# Generated by Django 4.1.6 on 2023-02-05 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplo01', '0003_alter_pessoa_options_pessoa_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(blank=True, default='1990-01-01', null=True, verbose_name='Nascimento'),
        ),
    ]
