# Generated by Django 3.1.5 on 2021-02-10 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210209_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='ano_pub',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='capa',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='idioma',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='sobrenome',
        ),
    ]
