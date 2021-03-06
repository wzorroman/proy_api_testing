# Generated by Django 2.2.7 on 2019-11-17 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('cuerpo', models.TextField(blank=True, null=True, verbose_name='Cuerpo')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='core.Author')),
            ],
        ),
    ]
