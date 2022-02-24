from django.shortcuts import render,redirect
from .forms import RegisterForm,CustomUserChangeForm
from .models import  CustomUser

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response,'account/register.html',{"form":form})


def user_update_form(response):
    if response.method == 'POST':
        user_profile = CustomUser.objects.get(username=response.user)
        form = CustomUserChangeForm(response.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    if response.method == 'GET':
        user_profile = CustomUser.objects.get(username=response.user)
        form = CustomUserChangeForm(instance=user_profile)

    return render(response, 'account/user-change.html',{'form':form})


def cabinet(response):
    current_user = response.user
    return render(response,'account/cabinet.html',{"username":current_user,
                                                    "full_name":current_user.first_name +
                                                                ' ' + current_user.last_name,
                                                   "date": current_user.date_joined,
                                                   "email": current_user.email,
                                                   "sex":current_user.sex,
                                                   "avatar":'/media'+current_user.avatar.url,
                                                   "specialization":current_user.specialization,
                                                   "age":current_user.age,
                                                   "status":current_user.status,})
