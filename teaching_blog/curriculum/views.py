from django.shortcuts import render
import django.views.generic

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect


class Lesson:
    pass


class LessonUpdateView(django.views.generic.UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model= Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'


