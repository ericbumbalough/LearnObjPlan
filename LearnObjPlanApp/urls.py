from django.urls import path
from . import views
urlpatterns = [
    path('<int:objective_id>/', views.objective_list, name='objective_list')
]
