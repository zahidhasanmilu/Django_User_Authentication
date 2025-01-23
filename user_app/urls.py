from django.urls import path
from . views import user_signup,Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', user_signup, name='signup'),
]
