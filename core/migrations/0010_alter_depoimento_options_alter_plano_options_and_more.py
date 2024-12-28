# Generated by Django 5.1.4 on 2024-12-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_depoimento_plano_alter_feature_icone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='depoimento',
            options={'verbose_name': 'Depoimento', 'verbose_name_plural': 'Depoimentos'},
        ),
        migrations.AlterModelOptions(
            name='plano',
            options={'verbose_name': 'Plano', 'verbose_name_plural': 'Planos'},
        ),
        migrations.AddField(
            model_name='plano',
            name='armazenamento_ilimitado',
            field=models.BooleanField(default=False, verbose_name='Armazenamento ilimitado?'),
        ),
        migrations.AddField(
            model_name='plano',
            name='numero_usuarios_ilimitado',
            field=models.BooleanField(default=False, verbose_name='Número de usuários ilimitado?'),
        ),
        migrations.AlterField(
            model_name='plano',
            name='armazenamento',
            field=models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Limite máximo de armazenamento (GB)'),
        ),
    ]