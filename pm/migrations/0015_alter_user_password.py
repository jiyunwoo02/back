# Generated by Django 5.0.6 on 2024-06-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0014_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$mxji2HOOarpfvbss2GfM9F$EpoMqFd/TxtkRoJGS1/IKptlIRutYA4cC3CeDkB3uss=', max_length=128),
        ),
    ]