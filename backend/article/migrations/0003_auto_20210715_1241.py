# Generated by Django 3.2.5 on 2021-07-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210715_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='praises',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
