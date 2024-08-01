from django.db import models
from django.contrib.auth.models import User


class Difbri_prof_user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=45, default='Name')
    photo = models.ImageField(upload_to='imag/', default='imag/profile.png')

    def __str__(self):
        return self.nickname

class Difbri_photo_lenta(models.Model):
    us = models.ForeignKey(Difbri_prof_user,on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='imag_lent/',default='')



class Difbri_user_quest(models.Model):
    us_q = models.ForeignKey(Difbri_prof_user, related_name='us_q', on_delete=models.CASCADE)
    cat= [
        ('physics', 'Физика'),
        ('math', 'Математика'),
        ('chemistry', 'Химия'),
        ('engineering_drawing', 'Черчение'),
        ('english', 'Английский язык'),
        ('belarusian_language', 'Белорусский язык'),
        ('belarusian_literature', 'Белорусская литература'),
        ('russian_language', 'Русский язык'),
        ('russian_literature', 'Русская литература'),
        ('computer_science', 'Информатика'),
        ('geography', 'География'),
        ('world_history', 'Всемирная история'),
        ('history_of_belarus', 'История Беларуси'),
        ('social_studies', 'Обществознание'),
        ('biology', 'Биология'),
    ]
    category = models.CharField(max_length=50, choices=cat)
    title = models.CharField(max_length=100)
    content = models.TextField()


class chat_mess(models.Model):
    us_chat1 = models.ForeignKey(Difbri_prof_user,related_name='us1',on_delete=models.CASCADE)
    us_chat2 = models.ForeignKey(Difbri_prof_user, related_name='us2', on_delete=models.CASCADE)
    text = models.TextField(default="")


class otvet_vopr(models.Model):
    us_utvet = models.ForeignKey(Difbri_prof_user,related_name='usotvet', on_delete=models.CASCADE)
    vopr = models.ForeignKey(Difbri_user_quest,related_name='otvet', on_delete=models.CASCADE)
    otvet = models.TextField(default="")
    kol_ot = models.IntegerField(default=0)
