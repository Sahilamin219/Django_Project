# Generated by Django 2.2.5 on 2020-09-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
    ]