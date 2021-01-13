from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet

from .models import UserCredits

# Create your views here.
@login_required(login_url = '/public/login')
def update(request: HttpRequest) -> HttpResponse:
    return render(request, 'administrator/update.html')

@login_required(login_url = '/public/login')
def update_submission(request: HttpRequest) -> HttpResponse:
    def encrypt(msg):
        key = Fernet.generate_key()
        f = Fernet(key)
        msg_enc = f.encrypt(msg.encode('utf-8'))
        return key.decode('utf-8'), msg_enc.decode('utf-8')
    user_update = User.objects.get(username=request.POST['username'])
    credits_list = []
    for i in range(1,5):
        for j in range(1,3):
            for k in range(1,7):
                input_name = str(i)+'-'+str(j)+'-'+str(k)
                credits_list.append(request.POST[input_name])
    
    credits_str = ''.join(credits_list)
    key, credits_str_enc = encrypt(credits_str)
    try:
        user_credits = UserCredits.objects.get(user = user_update)
    except UserCredits.DoesNotExist:
        user_credits = UserCredits(user=user_update)
    user_credits.credits = credits_str_enc
    user_credits.key = key
    user_credits.save()

    return render(request, 'administrator/update.html')