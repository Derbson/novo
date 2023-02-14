# Generated by Django 4.1.6 on 2023-02-14 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ftografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('categoria', models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('publicado', models.BooleanField(default=False)),
                ('data_fotografia', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
