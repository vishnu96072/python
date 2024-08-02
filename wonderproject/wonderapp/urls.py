from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('wonder/<int:wonder_id>/',views.detail,name='detail'),
    path('add/',views.add_wonder,name='add_wonder'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]