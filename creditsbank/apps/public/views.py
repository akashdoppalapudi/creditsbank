from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from num2words import num2words
from cryptography.fernet import Fernet

from .models import UserData
from creditsbank.apps.administrator.models import UserCredits

# helper function
def decrypt(key, msg_enc):
    f = Fernet(key.encode('utf-8'))
    msg_dec = f.decrypt(msg_enc.encode('utf-8')).decode('utf-8')
    return msg_dec

# Create your views here.
@login_required(login_url='/public/login')
def profile(request: HttpRequest) -> HttpResponse:
    try:
        if request.user.is_superuser or request.user.is_staff:
            context = {}
        else:
            num = [num2words(i).replace('-', '', 1) for i in range(1,49)]
            user_credits = UserCredits.objects.get(user = request.user)
            credits_enc = user_credits.credits
            key = user_credits.key
            credits_str = decrypt(key, credits_enc)
            grade_pts = {'O':10, 'S':9, 'A':8, 'B':7, 'C':6, 'D':5, 'F':0, '':0}
            credit_list = [i for i in credits_str]+['' for j in range(48-len(credits_str))]
            total_points = 0
            for i in credit_list:
                total_points = total_points+grade_pts[i]
            cgpa = total_points/len(credits_str)
            user_credits = dict(zip(num, credit_list))
            obj = UserData.objects.get(user = request.user)
            context = {
            'course' : obj.course,
            'branch' : obj.branch,
            'cgpa' : round(cgpa, 2),
            }
            context.update(user_credits)
        return render(request, 'public/profile.html', context)
    except UserCredits.DoesNotExist:
        return HttpResponse("<h2>Your Data does not Exists<h2>")