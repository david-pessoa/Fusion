# Generated by Django 5.1.4 on 2024-12-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_depoimento_options_alter_plano_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='depoimento',
            name='descricao',
            field=models.TextField(default='Praesent cursus nulla non arcu tempor, ut egestas elit tempus. In ac ex fermentum, gravida felis nec, tincidunt ligula.', max_length=500, verbose_name='Descrição'),
        ),
    ]
