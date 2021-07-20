from django.contrib import admin

from .models import Course, Origin, ContentArea, Objective

admin.site.register(Course)
admin.site.register(Origin)
admin.site.register(ContentArea)
admin.site.register(Objective)
