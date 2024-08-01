# Generated by Django 5.0.6 on 2024-06-17 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Difbri', '0009_difbri_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difbri_friend',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='Difbri.difbri_prof_user'),
        ),
        migrations.AlterField(
            model_name='difbri_friend',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='Difbri.difbri_prof_user'),
        ),
    ]