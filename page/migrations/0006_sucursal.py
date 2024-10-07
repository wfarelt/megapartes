# Generated by Django 5.0.4 on 2024-10-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='sucursales/')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
    ]