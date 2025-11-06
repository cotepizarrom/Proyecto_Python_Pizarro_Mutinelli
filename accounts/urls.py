from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, profile_view, profile_edit_view

urlpatterns = [
    path('login/',  auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),

    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),

    path('password/change/',
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    path('password/change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
]

from django.contrib.auth import views as auth_views

path(
    'logout/',
    auth_views.LogoutView.as_view(next_page='home'),
    name='logout'
),