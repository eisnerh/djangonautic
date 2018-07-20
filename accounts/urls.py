from django.urls import path

from accounts.views import sign_up_views, login_views, logout_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', sign_up_views, name='sing_up'),
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
]
