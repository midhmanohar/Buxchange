# Generated by Django 2.1.2 on 2018-11-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181104_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
