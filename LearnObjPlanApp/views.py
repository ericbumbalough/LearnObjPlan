from django.shortcuts import render

from .models import Objective


def objective_list(request, objective_id):
    context = {
        'objective': Objective.objects.get(id=objective_id)
    }
    return render(request, 'LearnObjPlanApp/objective.html', context)
