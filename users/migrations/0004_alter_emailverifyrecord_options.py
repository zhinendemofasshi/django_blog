# Generated by Django 4.1.3 on 2022-12-04 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': 'Captcha', 'verbose_name_plural': 'Captcha'},
        ),
    ]
