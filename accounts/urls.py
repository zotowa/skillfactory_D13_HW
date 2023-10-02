from django.contrib.auth.views import PasswordResetView
from django.urls import path, include

from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('confirm/<int:code_id>/', confirm, name='confirm'),
    path('reset', reset, name='reset'),
]
