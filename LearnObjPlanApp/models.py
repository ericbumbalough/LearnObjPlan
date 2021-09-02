from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

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

class User(AbstractUser):
    pass


class Course(models.Model):
    name = models.CharField(max_length=200, help_text=course_name_help)
    number = models.CharField(max_length=200, help_text=course_number_help)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.number

class Learning_Activity(models.Model):
    learning_activity = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    descripton = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE) 
    
    def __str__(self):
        return self.learning_activity
    
    
class Assessment(models.Model):
    assessment = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    descripton = models.TextField(blank=True) 
    user = models.ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return self.assessment


class Objective(models.Model):
    objective = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    parents = models.ManyToManyField('self',
                                     blank=True,
                                     help_text=parents_help,
                                     symmetrical=False,
                                     related_name='parents_related')
    # children = models.ManyToManyField('self',
    #                                   blank=True,
    #                                   help_text=children_help,
    #                                   symmetrical=False,
    #                                   related_name='children_related')
    assessments = models.ForeignKey(Assessment,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    learning_activities = models.ForeignKey(Learning_Activity,
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return self.objective
    
    