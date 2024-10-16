from django.urls import path, include

from users.views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('log_out/', log_out, name='log_out'),
    path('register/', Register.as_view(), name='register'),
    path('states/', state_list, name='state_list'),
    
]
