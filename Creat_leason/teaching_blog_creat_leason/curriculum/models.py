from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os

# Create models .
class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lessons')
    name = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name="Video", blank=True, null=True)
    ppt = models.FileField(upload_to=save_lesson_files,verbose_name="Presentations", blank=True)
    Notes = models.FileField(upload_to=save_lesson_files,verbose_name="Notes", blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('curriculum:lesson_list', kwargs={'slug':self.subject.slug, 'standard':self.Standard.slug})

