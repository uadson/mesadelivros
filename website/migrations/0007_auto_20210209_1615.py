# Generated by Django 3.1.5 on 2021-02-09 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210205_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='imagem',
            new_name='capa',
        ),
    ]