# Generated by Django 3.0.8 on 2021-02-12 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210211_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='ARTICLE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atricle', models.CharField(max_length=400)),
                ('img', models.ImageField(upload_to='uploads/')),
                ('title', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.USER')),
            ],
        ),
        migrations.DeleteModel(
            name='Artical',
        ),
    ]
