from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Programs
from .serializers import ProgramSerializer


@api_view(['GET'])
def get_all_programs(request):
    programs = Programs.objects.all()
    serializer = ProgramSerializer(programs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_program_by_id(request, program_id):
    try:
        program = Programs.objects.get(id=program_id)
    except Programs.DoesNotExist: 
        return Response({"Error": "Program Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProgramSerializer(program)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_program(request):
    if request.method == 'POST':
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_program(request, program_id):
    try:
        program = ProgramSerializer.objects.get(id=program_id)
    except Programs.DoesNotExist:
        return Response({"Error":"Program Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProgramSerializer(program, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_program(request, program_id):
    try:
        program = Programs.objects.get(id=program_id)
    except Programs.DoesNotExist:
        return Response({"Error":"Program Not Found"}, status=status.HTTP_404_NOT_FOUND)

    program.delete()
    return Response({"Message":"Program deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
