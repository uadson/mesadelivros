# Generated by Django 3.1.5 on 2021-02-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]