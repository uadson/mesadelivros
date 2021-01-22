# Generated by Django 3.1.5 on 2021-01-22 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=50)),
                ('ano_pub', models.DateField(default=0)),
                ('idioma', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.categoria')),
            ],
        ),
    ]