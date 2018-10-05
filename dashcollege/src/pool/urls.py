from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'pool'
urlpatterns = [
    path('pool/', views.Pool.as_view(), name='pool'),
    # path('resource', views.PoolResource.as_view(), name='edit_self'),
]