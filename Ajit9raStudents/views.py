from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import AddStudentSerializer


@api_view(['GET'])
def get_all_students(request):
    students = Students.objects.all()
    serializer = AddStudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_student_by_id(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
    except Students.DoesNotExist: 
        return Response({"Error": "Student Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AddStudentSerializer(student)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        serializer = AddStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_student(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
    except Students.DoesNotExist:
        return Response({"Error":"Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AddStudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
    except Students.DoesNotExist:
        return Response({"Error":"Student Not Found"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({"Message":"Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
