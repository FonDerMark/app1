# Generated by Django 4.1.7 on 2023-02-15 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptography_', '0003_alter_cryptofile_encoded'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CryptoFile',
        ),
    ]
