from django.shortcuts import render
import django.views.generic

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect


         
class LessonUpdateView(django.views.generic.UpdateView):
    fields = ('name','position','video','ppt','Notes')
    model= Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'

class LessonDeleteView(django.views.generic.DeleteView):
    model= Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':subject.slug})
