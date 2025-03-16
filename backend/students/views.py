from django.http import JsonResponse
from .models import Student

def insert_student(request):
    student = Student(name="abc", rollnumber=43, age=12)
    student.save()
    return JsonResponse({"message": "Student inserted successfully!", "student_id": student.id})
