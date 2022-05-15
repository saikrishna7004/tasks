from django.contrib import admin

from tasklist.models import Answer, Question, Section, TaskInfo

# Register your models here.

admin.site.register(TaskInfo)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Answer)