from django.shortcuts import render


# Create your views here.


def sign_up_views(request):
    return render(request, 'accounts/sing_up.html')
