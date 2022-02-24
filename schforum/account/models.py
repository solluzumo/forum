from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    username = models.CharField("Юзернейм",max_length=15,unique=True)
    status = models.CharField("Статус",max_length=30,default="Статус пользователя")
    email = models.EmailField("Эл.почта",max_length=254)
    first_name = models.CharField("Имя",max_length=20)
    last_name = models.CharField("Фамилия",max_length=20)
    password1 = models.CharField("Пароль",max_length=30)
    password2 = models.CharField("Подтверждение пароля",max_length=30)
    sex = models.CharField("Пол",max_length=30,blank= True,default="Не указан")
    avatar = models.ImageField("Аватар профиля", default='default_profile_image.png',blank= True)
    specialization = models.CharField("Ваша специиальность/профессия",max_length=50,
                                            null=True,blank= True,default="Не указана")
    age = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.username

