# Generated by Django 3.1.5 on 2021-02-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210205_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano_pub',
            field=models.DateField(default=2021),
        ),
    ]