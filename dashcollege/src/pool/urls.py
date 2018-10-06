from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'pool'
urlpatterns = [
    path('pool/', views.Pool.as_view(), name='pool'),
    path('pool/cab/', views.Pool.as_view(), name='cab'),
    path('pool/food/', views.Pool.as_view(), name='food'),
    path('pool/others/', views.Pool.as_view(), name='others'),
    path('store/', views.Pool.as_view(), name='store'),
    path('find/', views.Pool.as_view(), name='store'),
    # path('resource', views.PoolResource.as_view(), name='edit_self'),
]