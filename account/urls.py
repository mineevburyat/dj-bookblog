from django.urls import path, include
from . import views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'account'


# TODO: в 5-ой версии выход нужно делать по POST запросу
# TODO: https://dev.to/earthcomfy/django-reset-password-3k0l
urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # url-адреса входа и выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # url-адреса смены пароля
    path('password-change/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('account:password_change_done')),
        name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # url-адреса сброса пароля
    path('password-reset/',views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/ password_reset_complete.html'), name='password_reset_complete'),
    # стандартная система аутентификации
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # index page
    path('', views.dashboard, name='dashboard'),
]