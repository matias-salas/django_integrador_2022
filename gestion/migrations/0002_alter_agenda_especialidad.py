# Generated by Django 3.2.14 on 2022-11-16 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='especialidad',
            field=models.CharField(choices=[('Dentistry', 'Dentistry'), ('Cardiology', 'Cardiology'), ('ENT Specialists', 'ENT Specialists'), ('Astrology', 'Astrology'), ('Neuroanatomy', 'Neuroanatomy'), ('Blood Screening', 'Blood Screening'), ('Eye Care', 'Eye Care'), ('Physical Therapy', 'Physical Therapy')], max_length=250),
        ),
    ]
