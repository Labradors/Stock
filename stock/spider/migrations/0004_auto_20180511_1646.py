# Generated by Django 2.0.5 on 2018-05-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0003_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
