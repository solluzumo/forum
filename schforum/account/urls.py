from django.urls import path,include
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from . import views as view
urlpatterns = [
    path('cabinet/update', view.user_update_form),
    path('cabinet',view.cabinet,name="cabinet_or_login"),
    path('register',view.register),
    path('password-change', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
