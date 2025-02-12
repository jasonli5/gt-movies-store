from django.urls import path
from . import views
from accounts.views import ResetPasswordView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('signup', views.signup, name='accounts.signup'),
     path('login/', views.login, name='accounts.login'),
     path('logout/', views.logout, name='accounts.logout'),
     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
     path('password-reset/done/',  
          CustomPasswordResetDoneView.as_view(),  
          name='password_reset_done'),  # ✅ Match this name to the reverse_lazy in views.py

     path(
        'password-reset-confirm/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
