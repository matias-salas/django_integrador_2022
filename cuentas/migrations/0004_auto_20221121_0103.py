# Generated by Django 3.2.14 on 2022-11-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
