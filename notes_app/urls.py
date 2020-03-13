from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('confirm',views.confirm_delete,name='confirm'),
    path('<int:note_id>/', views.details, name='details')
]
