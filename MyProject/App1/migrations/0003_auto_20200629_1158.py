# Generated by Django 3.0.7 on 2020-06-29 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_auto_20200629_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='branch',
            field=models.CharField(default=20, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='demo',
            name='age',
            field=models.IntegerField(blank=True, default=20),
        ),
    ]