from django.urls import path
from . import views

urlpatterns=[
    path('', views.teacherindex,name='teacherindex'),
    path('addteacher/', views.teacher_add,name='teacher_add'),
    path('removeteacher/', views.teacher_remove,name='teacher_remove'),
]
