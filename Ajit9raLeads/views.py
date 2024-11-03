from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import AddLeadSerializer


@api_view(['GET'])
def get_all_leads(request):
    leads = Lead.objects.all()
    serializer = AddLeadSerializer(leads, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_lead_by_id(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist: 
        return Response({"Error": "Lead Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = AddLeadSerializer(lead)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_lead(request):
    if request.method == 'POST':
        serializer = AddLeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_lead(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return Response({"Error":"Lead Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AddLeadSerializer(lead, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_lead(request, lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return Response({"Error":"Lead Not Found"}, status=status.HTTP_404_NOT_FOUND)

    lead.delete()
    return Response({"Message":"Lead deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
