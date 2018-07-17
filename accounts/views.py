from django.contrib.auth.forms import UserCreationForm
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
