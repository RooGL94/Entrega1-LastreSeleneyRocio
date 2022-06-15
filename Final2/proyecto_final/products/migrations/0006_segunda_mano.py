# Generated by Django 4.0.4 on 2022-06-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_ofertas'),
    ]

    operations = [
        migrations.CreateModel(
            name='segunda_mano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('detalles', models.CharField(max_length=150)),
                ('imagen', models.ImageField(null=True, upload_to='productos_imagenes')),
            ],
            options={
                'verbose_name': 'segunda mano',
            },
        ),
    ]
