# Generated by Django 3.1 on 2021-03-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]