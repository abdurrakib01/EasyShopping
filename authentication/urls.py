from django.urls import path
from .views import UserRegisterView, CustomerProfileView, UserProfileView
from django.contrib.auth import views as auth_views
from .form import (
    UserLoginForm, 
    UserPasswordChangeForm, 
    MyPasswordResetForm, 
    MySetPasswordForm)

urlpatterns = [
    path('accounts/register/', UserRegisterView.as_view(), name='user-register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='auth/login.html',
        authentication_form=UserLoginForm), name='user-login'),
    path('user/profile/', UserProfileView.as_view(), name='profile'),
    path('user/address/', CustomerProfileView.as_view(), name="address"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='user-login'), name='user-logout'),
    path('user/changepassword/', auth_views.PasswordChangeView.as_view(
        template_name="auth/changePassword.html",
        form_class=UserPasswordChangeForm,
        success_url="/user/passwordchangedone/"
        ),
        name="change-pass"
    ),
    path('user/passwordchangedone/', auth_views.PasswordChangeView.as_view(
        template_name="auth/changePasswordDone.html",
        ),
        name="passwordchangedone"
    ),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name = "auth/password_reset.html",
        form_class = MyPasswordResetForm,
        ),
         name='password_reset'
    ),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = "auth/password_reset_done.html",
        ),
        name='password_reset_done'
    ),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'auth/password_reset_confirm.html',
        form_class=MySetPasswordForm,
        ),
        name='password_reset_confirm'
    ),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name = "auth/password_reset_complete.html",
        ),
         name='password_reset_complete'
    ),
]
