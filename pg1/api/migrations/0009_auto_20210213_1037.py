# Generated by Django 3.0.8 on 2021-02-13 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210212_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='atricle',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.USER'),
        ),
    ]
