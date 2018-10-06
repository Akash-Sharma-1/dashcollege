from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'pool'
urlpatterns = [
    path('pool/', views.Pool.as_view(), name='pool'),
    path('pool/cab/', views.PoolCab.as_view(), name='cab'),
    path('pool/food/', views.PoolFood.as_view(), name='food'),
    path('pool/others/', views.PoolMisc.as_view(), name='others'),
    path('store/', views.Store.as_view(), name='store'),
    path('find/', views.Find.as_view(), name='find'),
    # path('resource', views.PoolResource.as_view(), name='edit_self'),
]