# Generated by Django 4.1.9 on 2023-05-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='miembro',
            field=models.CharField(default='null', max_length=30),
            preserve_default=False,
        ),
    ]