from django.urls import path
from . import views

app_name = 'pool'
urlpatterns = [
    path('pool/', views.PoolPage.as_view(), name='show_self'),
    path('pool/resource/', views.PoolResource.as_view(), name='edit_self'),
]