from django.urls import path
from .views import insert_student

urlpatterns = [
    path('insert-student/', insert_student),
]
