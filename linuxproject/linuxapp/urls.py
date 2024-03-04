from django.urls import path
from linuxapp import views

app_name = 'linuxapp'

urlpatterns=[
    path("register/",views.register,name='register'),
    path("user_login/",views.user_login,name='user_login')
]
