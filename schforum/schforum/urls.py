from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('forum.urls')),
    path('account/', include('account.urls')),
    path('', include("django.contrib.auth.urls"), name="login"),

]
