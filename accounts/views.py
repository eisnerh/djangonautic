from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.


def sign_up_views(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #
            # log the user in
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sing_up.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('articles:article_list')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
