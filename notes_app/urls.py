from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_note',views.new_note,name='new_note'),
    path('<int:note_id>/', views.details, name='details'),
    path('<int:note_id>/confirm_delete',views.confirm_delete,name='confirm_delete')
]
