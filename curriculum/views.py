from django.shortcuts import render
from django.views.generic import ( ListView)


from .models import Subject


class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'


