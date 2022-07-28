from django.urls import path

from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

app_name = "users"
urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', signup, name='signup'),
    #path('profile/<str:username>', profile_page, name='profile'),
    # path('profile/<pk>', login_required(ProfileView.as_view()), name = 'profile'),
    # path('accounts/', account_list, name='signup'),
    # path('accounts/<int:pk>', account),
    # path('login/', login, name='login'),
    # path('auth', include('rest_framework.urls', namespace='rest_framework'))
]