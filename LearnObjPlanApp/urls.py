from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<slug:course_slug>/', views.ObjectiveList.as_view(), name='objective_list')
]
