# Generated by Django 2.1.5 on 2019-01-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190111_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
