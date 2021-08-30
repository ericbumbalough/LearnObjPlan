from django.contrib import admin

from .models import Assessment, Learning_Activity, Objective, Course

admin.site.register(Objective)
admin.site.register(Assessment)
admin.site.register(Learning_Activity)
admin.site.register(Course)