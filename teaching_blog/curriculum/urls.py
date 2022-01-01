from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [

    path('<str:standard>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(),name='lesson_update'),
    path('<str:standard>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(),name='lesson_delete'),

]
