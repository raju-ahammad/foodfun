# Generated by Django 2.2.5 on 2019-10-05 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conatct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
