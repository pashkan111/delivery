from rest_framework.views import APIView
from tracking.models import Tracking
from django.views.generic.list import ListView
from.serializers import TrackingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


class Search(ListView):
    model = Tracking()
    template_name = 'tracking.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        object_list = Tracking.objects.filter(tracking_number_client__icontains=query)
        return object_list
    

@api_view(['GET', 'POST'])
def create_consignment_trackstatus(request):  
    if request.method == 'GET':
        trackstatus_consignments = Tracking.objects.all()
        trackstatus_consignments_serializer = TrackingSerializer(trackstatus_consignments, many=True)
        return JsonResponse(trackstatus_consignments_serializer.data, safe=False)

    elif request.method == 'POST':
        trackstatus_consignment_data = JSONParser().parse(request)
        trackstatus_consignments_serializer = TrackingSerializer(data=trackstatus_consignment_data, many=True)
        if trackstatus_consignments_serializer.is_valid():
            trackstatus_consignments_serializer.save()
            return JsonResponse(trackstatus_consignments_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(trackstatus_consignments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Trak(APIView):
    def post(self, request):
        data = request.data
        print(data)
        tracking_number_client = data.get('trak', '')
        if tracking_number_client:
            object = Tracking.objects.filter(tracking_number_client=tracking_number_client)
            if not object:
                message = {'status': 'trak not found'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            object = object.first()
            result = TrackingSerializer(object)
            return Response(result.data, status=status.HTTP_200_OK)
        message = {'status': 'no data'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT'])
def consignment_detail_trackstatus(request, pk):
    try:
        trackstatus_consignment = Tracking.objects.get(pk=pk)
    except Tracking.DoesNotExist:
        return JsonResponse({'message': 'Накладной не существует'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        trackstatus_consignment_data = JSONParser().parse(request)
        trackstatus_consignments_serializer = TrackingSerializer(trackstatus_consignment, data=trackstatus_consignment_data)
        if trackstatus_consignments_serializer.is_valid():
            trackstatus_consignments_serializer.save()
            return JsonResponse(trackstatus_consignments_serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(trackstatus_consignments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
