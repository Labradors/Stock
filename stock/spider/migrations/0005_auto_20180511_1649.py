# Generated by Django 2.0.5 on 2018-05-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0004_auto_20180511_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='id',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False),
        ),
    ]