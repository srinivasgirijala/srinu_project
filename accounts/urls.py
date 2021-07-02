from django.urls import path
from.import views

urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('contact',views.contact,name="contact"),
    path('About',views.About,name="About"),
    path('careers',views.careers,name="careers"),
    path('created',views.created,name="created"),
    path('become',views.become,name="become"),
    path('training',views.training,name="training"),
    path('technologies',views.technologies,name="technologies")
]
