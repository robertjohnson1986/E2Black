# Generated by Django 2.2.5 on 2021-07-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E2BlackApp', '0005_auto_20210724_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='category',
            new_name='electrical',
        ),
        migrations.AddField(
            model_name='books',
            name='garden',
            field=models.CharField(default='Text', max_length=255),
        ),
        migrations.AddField(
            model_name='books',
            name='other',
            field=models.CharField(default='Text', max_length=255),
        ),
        migrations.AddField(
            model_name='books',
            name='pet_care',
            field=models.CharField(default='Text', max_length=255),
        ),
    ]