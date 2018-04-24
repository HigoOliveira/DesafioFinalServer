from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.authtoken import views as drf_views

from api import views

urlpatterns = [
    path('auth', drf_views.obtain_auth_token, name='auth'),
    re_path('verify-user-exists/(?P<phone>\+\d+)/$', views.UserVerify.as_view()),
    path('signup', views.Create.as_view()),
    path('user/update', views.Update.as_view()),
]