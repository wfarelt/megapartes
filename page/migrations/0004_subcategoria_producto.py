# Generated by Django 5.0.4 on 2024-10-28 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_ejecutivo_sucursal'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='page.categoria')),
            ],
            options={
                'verbose_name_plural': 'SubCategorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(default='productos/default.png', upload_to='productos/')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='page.subcategoria')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
