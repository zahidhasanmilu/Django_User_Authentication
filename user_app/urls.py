from django.urls import path
from .views import Home,user_signup,user_login,user_logout

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
