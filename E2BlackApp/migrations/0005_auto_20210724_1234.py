# Generated by Django 2.2.5 on 2021-07-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E2BlackApp', '0004_auto_20210717_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(default='Text', max_length=255),
        ),
        migrations.AddField(
            model_name='books',
            name='location',
            field=models.CharField(default='Text', max_length=255),
        ),
    ]
