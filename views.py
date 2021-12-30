from django.shortcuts import render
from django.views.generic import ( DetailView)

from .models import  Subject
from django.urls import reverse_lazy
from .forms import CommentForm,ReplyForm, LessonForm
from django.http import HttpResponseRedirect






# Azam part 1
class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'

# Azam part 1 end


