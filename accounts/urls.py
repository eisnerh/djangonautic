from django.urls import path

from accounts.views import sign_up_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', sign_up_views, name='sing_up'),
]
