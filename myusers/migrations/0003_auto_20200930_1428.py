# Generated by Django 2.2.5 on 2020-09-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0002_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='name',
        ),
        migrations.AddField(
            model_name='hero',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
