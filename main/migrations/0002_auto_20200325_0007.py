# Generated by Django 3.0.4 on 2020-03-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ID_user',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
