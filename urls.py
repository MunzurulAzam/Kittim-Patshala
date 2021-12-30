from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [

    path('<str:standard>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),

]
