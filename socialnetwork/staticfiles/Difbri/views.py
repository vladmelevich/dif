from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Difbri_prof_user, Difbri_photo_lenta,Difbri_user_quest,chat_mess,otvet_vopr
from django.db.models import Q
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password != password2:
            error_message = 'Пароли не совпадают'
            return render(request, 'register.html',{'error_message':error_message})
        elif User.objects.filter(email=email).exists():
            error_message = 'Пользователь с таким email уже существует'
            return render(request, 'register.html', {'error_message': error_message})
        else:
            user = User(username=name,email=email, password=password)
            user.set_password(password)
            user.save()
            return redirect('log_in')
    return render(request, 'register.html')

def auth(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('em')
        password = request.POST.get('pass')
        user = authenticate(request,username=name, email=email,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Неверный Email либо пароль'
            return render(request, 'log_in.html',{'error_message':error_message})
    return render(request, 'log_in.html')


def home(request):
    try:
        u = Difbri_prof_user.objects.get(user=request.user)
    except Difbri_prof_user.DoesNotExist:
        u = Difbri_prof_user.objects.create(user=request.user)
        u.save()

    if request.method == 'POST':
        if 'wheres' in request.POST:
            search_query = request.POST.get('wheres')
            difbri_us_all_q = Difbri_user_quest.objects.filter(title=search_query)
        else:
            category = request.POST.get('subject')
            title = request.POST.get('title')
            content = request.POST.get('content')

            try:
                dif_prof_user = Difbri_prof_user.objects.get(user=request.user)
            except Difbri_prof_user.DoesNotExist:
                dif_prof_user = Difbri_prof_user(user=request.user)
                dif_prof_user.save()

            dif_us_q = Difbri_user_quest(us_q=dif_prof_user, category=category, title=title, content=content)
            dif_us_q.save()
            difbri_us_all_q = Difbri_user_quest.objects.all()
    else:
        category = request.GET.get('subject')
        if category:
            difbri_us_all_q = Difbri_user_quest.objects.filter(category=category)
        else:
            difbri_us_all_q = Difbri_user_quest.objects.all()

    return render(request, 'home.html', {'duaq': difbri_us_all_q, 'u': u})

def his_prof(request,user_id):
    u1 = Difbri_prof_user.objects.get(user=request.user)
    try:
        his_prof = Difbri_prof_user.objects.get(user__id=user_id)
    except Difbri_prof_user.DoesNotExist:
        return HttpResponse('Профиль пользователя не найден')
    us_photo = Difbri_photo_lenta.objects.filter(us=his_prof)
    return render(request, 'his_profile.html',{'his_prof':his_prof,'us_photo':us_photo,'uq':u1})

def chat_friend(request):
    chat_fri = Difbri_prof_user.objects.get(user=request.user)
    chat_f = chat_mess.objects.filter(Q(us_chat1=chat_fri)|Q(us_chat2=chat_fri))

    friend = []
    for i in chat_f:
        if i.us_chat1 == chat_fri:
            friend.append(i.us_chat2)
        else:
            friend.append(i.us_chat1)

    friend = set(friend)
    return render(request,'chat_friend.html',{'friend':friend,'chat_fri':chat_fri})


def chat(request, user_id):
    user1 = Difbri_prof_user.objects.get(user=request.user)
    user2 =Difbri_prof_user.objects.get(user__id=user_id)

    if request.method == 'POST':
        text = request.POST.get('chat')
        if text:
            chat_message = chat_mess(us_chat1=user1, us_chat2=user2, text=text)
            chat_message.save()

    messages = chat_mess.objects.filter(
        (Q(us_chat1=user1) & Q(us_chat2=user2)) |
        (Q(us_chat1=user2) & Q(us_chat2=user1))
    ).order_by('id')

    return render(request, 'messager.html', {'user2': user2, 'messages': messages,'chat':user1})
@login_required()
def prof(request):
    try:
        pro = Difbri_prof_user.objects.get(user=request.user)
    except Difbri_prof_user.DoesNotExist:
        pro = Difbri_prof_user.objects.create(user=request.user)
        pro.save()

    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        if nickname:
            pro.nickname=nickname
        photo = request.FILES.get('photos')
        if photo:
            pro.photo = photo
        pro.save()
        photo_le = request.FILES.get('photo_lenta')
        if photo_le:
            Difbri_photo_lenta.objects.create(photos=photo_le, us=pro)

    try:
        photo_let = Difbri_photo_lenta.objects.filter(us=pro)
        if photo_let:
            photo_let = photo_let.all()
        else:
            photo_let = None
    except:
        photo_let = None

    return render(request, 'profile.html',{'prof':pro,'photo_let':photo_let})


def quations(request,quation_id):
    pols = Difbri_prof_user.objects.get(user=request.user)
    vopr = Difbri_user_quest.objects.get(id=quation_id)
    if request.method == 'POST':
        otvet = request.POST.get('otvet')
        if otvet:
            otvet_vopr.objects.create(us_utvet=pols,vopr=vopr,otvet=otvet)
    ot = otvet_vopr.objects.filter(vopr__id=quation_id)
    return render(request,'quations.html',{'vopr':vopr, 'ot':ot})

def lider(request):
    return render(request,'lider.html')

def difbri(request):
    try:
        ue = Difbri_prof_user.objects.get(user=request.user)
    except Difbri_prof_user.DoesNotExist:
        ue = Difbri_prof_user.objects.create(user=request.user)
        ue.save()
    return render(request,'onas.html',{'ue':ue})