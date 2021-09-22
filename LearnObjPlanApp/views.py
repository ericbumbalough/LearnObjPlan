from django.views import generic
from .models import Objective, Course
from Accounts.models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin


class ObjectiveList(LoginRequiredMixin, generic.ListView):
    '''List of all objectives for user'''
    model = Objective
    template_name = 'objective_list.html'
    
    def get_queryset(self):
        return Objective.objects.filter(user=self.request.user).filter(top_level=True)

class CourseList(LoginRequiredMixin, generic.ListView):
    '''List of all courses for a user'''
    model = Course
    template_name = 'course_list.html'
    
    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)
    