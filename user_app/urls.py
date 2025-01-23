from django.urls import path
from .views import Home,user_signup

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', user_signup, name='signup'),
]
