from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from Accounts.models import CustomUser as User

# TODO these will come from locale files

parents_help = ('Is this requirement devirived different requirements?'
                + ' If so, put that requirement here. If not, leave blank.'
                + ' If you input parents, the system will automatically add '
                + 'childern when you save.')
children_help = ('Are other requirements derived from this one? '
                 + 'If so, put them here. If not, leave blank.'
                 + ' If you input children, the system will automatically add '
                 + 'parents when you save.')
course_name_help = 'Example: College Algebra'
course_number_help = 'Example: MATH 136'

class Course(models.Model):
    name = models.CharField(max_length=200, help_text=course_name_help)
    number = models.CharField(max_length=200, help_text=course_number_help)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.number

class Learning_Activity(models.Model):
    learning_activity = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    descripton = models.TextField(blank=True)
        
    def __str__(self):
        return self.learning_activity
    
    
class Assessment(models.Model):
    assessment = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    descripton = models.TextField(blank=True) 
    
    def __str__(self):
        return self.assessment


class Objective(models.Model):
    objective = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    # parents = models.ManyToManyField('self',
    #                                  blank=True,
    #                                  help_text=parents_help,
    #                                  symmetrical=False,
    #                                  related_name='parents_related')
    children = models.ManyToManyField('self',
                                      blank=True,
                                      help_text=children_help,
                                      symmetrical=False,
                                      related_name='children_related')
    # top_level is a temporary way to flag the uppermost level objectives
    # will be replaced by the closure table or something eventually
    # also need to update queryset in views.py
    top_level = models.BooleanField(default=False)
    assessments = models.ManyToManyField(Assessment,
                                         blank=True,
                                         related_name='assessment_related')
    learning_activities = models.ManyToManyField(Learning_Activity,
                                                 blank=True,
                                                 related_name='learning_activities_related')
    notes = models.TextField(blank=True)
        
    def __str__(self):
        return self.objective
    
    