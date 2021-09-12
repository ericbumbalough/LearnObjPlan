from django.views import generic
from .models import Objective
from Accounts.models import CustomUser as User
from django.contrib.auth.mixins import LoginRequiredMixin


class ObjectiveList(LoginRequiredMixin, generic.ListView):
    '''List of all objectives for user'''
    model = Objective
    template_name = 'objective_list.html'
    
    def get_queryset(self):
        return Objective.objects.filter(user=self.request.user)
