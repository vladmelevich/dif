from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='h'),
    path('home/', views.home, name='home'),
    path('his_profile/<int:user_id>', views.his_prof, name='his_profile'),
    path('log_in/', views.auth, name='log_in'),
    path('register/', views.reg, name='reg'),
    path('profile/', views.prof, name='profile'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    path('chat_friend',views.chat_friend, name='chat_friend'),
    path('otvet/<int:quation_id>',views.quations, name='otvet'),
    path('lider/',views.lider, name='lider'),
    path('difbri/',views.difbri, name='difbri'),
]
