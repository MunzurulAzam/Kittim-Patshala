from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [

    path('<str:standard>/<str:slug>/create/', views.LessonCreateView.as_view(),name='lesson_create'),

]
