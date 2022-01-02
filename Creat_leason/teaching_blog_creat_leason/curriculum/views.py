import Subject as Subject
from django.shortcuts import render
from django.views.generic import (CreateView)


from django.urls import reverse_lazy
from .forms import LessonForm
from django.http import HttpResponseRedirect


class LessonCreateView(CreateView):
    """
    Provide a way to show and handle a ModelForm in a request.
    """
    fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = LessonForm
    context_object_name = 'subject'
    model= Subject
    template_name = 'curriculum/lesson_create.html'

    """
    Return the URL to redirect to after processing a valid form.
    """
    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})

    """
    If the form is valid, save the associated model.
    """
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


