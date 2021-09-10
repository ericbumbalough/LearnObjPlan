from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Assessment, Learning_Activity, Objective, Course

admin.site.register(Objective)
admin.site.register(Assessment)
admin.site.register(Learning_Activity)
admin.site.register(Course)