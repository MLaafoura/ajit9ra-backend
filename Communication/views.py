from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Communication
from .serializers import CommunicationSerializer



@api_view(['GET'])
def get_all_communcations(request):
    communication = Communication.objects.all()
    serializer = CommunicationSerializer(communication, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
'''
@api_view(['GET'])
def get_communication_by_id(request, communication_id):
    try:
        communication = Communication.objects.get(id=communication_id)
    except Communication.DoesNotExist: 
        return Response({"Error": "Communication Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommunicationSerializer(communication)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
'''

@api_view(['GET'])
def get_communication_by_lead_id(request, lead_id):
    communications = Communication.objects.filter(lead_id=lead_id)
    if not communications.exists():
        return Response({"Error": "No communications found for this lead"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommunicationSerializer(communications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_communication(request):
    if request.method == 'POST':
        serializer = CommunicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_communication(request, communication_id):
    try:
        communication = Communication.objects.get(id=communication_id)
    except Communication.DoesNotExist:
        return Response({"Error":"Communication Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CommunicationSerializer(communication, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_communication(request, communication_id):
    try:
        communication = Communication.objects.get(id=communication_id)
    except Communication.DoesNotExist:
        return Response({"Error":"Communication Not Found"}, status=status.HTTP_404_NOT_FOUND)

    communication.delete()
    return Response({"Message":"Communication deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



