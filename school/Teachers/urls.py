
from django.urls import path
from .import views



urlpatterns = [
    path('',views.teacher_list, name ='all-teachers'),
    path('addteacher/',views.add_teacher, name="addteacher"),
    path('update-teacher/<str:id>/', views.update_teacher, name='update'),
    path('delete/<str:id>/', views.delete_teacher, name="delete"),
    path('manager/', views.manager_dashboard, name='manager-dashboard')
]