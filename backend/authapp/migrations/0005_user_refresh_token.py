# Generated by Django 3.2.5 on 2021-07-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_country_sticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
