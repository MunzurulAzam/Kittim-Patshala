from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                    ListView, CreateView,
                                    UpdateView,DeleteView,FormView,)
from .models import Standard, Subject, Lesson, Comment, WorkingDays, TimeSlots
from django.urls import reverse_lazy
from .forms import CommentForm,ReplyForm, LessonForm
from django.http import HttpResponseRedirect

class LessonListView(DetailView):
    """
        Provide the ability to retrieve a single object for further manipulation.
     """
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'
