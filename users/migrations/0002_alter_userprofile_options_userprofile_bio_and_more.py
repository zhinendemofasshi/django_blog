# Generated by Django 4.1.3 on 2022-12-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'UserProfile', 'verbose_name_plural': 'UserProfile'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='feature',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='feature'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6, verbose_name='gender'),
        ),
    ]
