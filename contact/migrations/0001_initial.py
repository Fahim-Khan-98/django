# Generated by Django 4.0 on 2022-06-19 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('subject', models.TextField(max_length=700)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
