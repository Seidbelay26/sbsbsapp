# Generated by Django 3.1.2 on 2021-08-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetme',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]