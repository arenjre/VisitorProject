from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker, Unit, Visit
from .serializers import UnitSerializer, VisitSerializer

# Create your views here.
class MakeUnit(APIView):
    def post(self, request):
        pass
    
class UnitsLinkedToWorker(APIView):
    def get(self, request):
        if 'phone_number' not in request.GET:
            return Response({'error': 'Worker phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        phone_number = request.GET['phone_number']
        try:
            import pdb;pdb.set_trace()
            worker = Worker.objects.get(phone_number=phone_number)
            units = Unit.objects.filter(worker=worker)
            serializer = UnitSerializer(units, many=True)
            return Response(serializer.data)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found.'}, status=status.HTTP_404_NOT_FOUND)
    

class MakeVisit(APIView):
    def post(self, request):
        if 'phone_number' not in request.data:
            return Response({'error': 'Worker phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if 'unit_pk' not in request.data or 'coordinates' not in request.data:
            return Response({'error': 'Unit PK and coordinates are required.'}, status=status.HTTP_400_BAD_REQUEST)

        phone_number = request.data['phone_number']
        unit_pk = request.data['unit_pk']
        coordinates = request.data['coordinates']
        try:
            worker = Worker.objects.get(phone_number=phone_number)
            unit = Unit.objects.get(pk=unit_pk, worker=worker)
            visit = Visit.objects.create(unit=unit, datetime=datetime.now(), latitude=coordinates['latitude'], longitude=coordinates['longitude'])
            serializer = VisitSerializer(visit)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Worker.DoesNotExist:
            return Response({'error': 'Worker not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Unit.DoesNotExist:
            return Response({'error': 'Unit not found or not linked to the worker.'}, status=status.HTTP_404_NOT_FOUND)

