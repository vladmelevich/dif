# Generated by Django 5.0.6 on 2024-06-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Difbri', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difbri_prof_user',
            name='nickname',
            field=models.CharField(default='Name', max_length=45),
        ),
        migrations.AlterField(
            model_name='difbri_prof_user',
            name='photo',
            field=models.ImageField(default='Ellipse 1.png', upload_to='imag/'),
        ),
    ]