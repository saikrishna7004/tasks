from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatewords

# Create your models here.

class TaskInfo(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "taskinfo"
        verbose_name_plural = "taskinfos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("taskinfo_detail", kwargs={"pk": self.pk})


class Section(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    task = models.ForeignKey(TaskInfo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "section"
        verbose_name_plural = "sections"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("section_detail", kwargs={"pk": self.pk})

class Question(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})
    
    @property
    def short_description(self):
        return truncatewords(self.desc, 5)

class Answer(models.Model):

    id = models.AutoField(primary_key=True)
    desc = models.TextField()
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

    def __str__(self):
        return self.desc

    def get_absolute_url(self):
        return reverse("answer_detail", kwargs={"pk": self.pk})
    
    @property
    def short_description(self):
        return truncatewords(self.desc, 5)
