from django.urls import path
from .views import Home,user_signup,user_login

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
]
