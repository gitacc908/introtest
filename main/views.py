from django.forms import FloatField
from .serializers import WorkerSerializer, VisitSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Worker, Store, Visit
from django.shortcuts import get_object_or_404
from .utils import get_phone


class WorkerStoreListView(APIView):
    serializer = WorkerSerializer

    def get(self, request, format=None):
        phone = request.data.get('phone')
        message = get_phone(phone)
        if message:
            return Response(message)
        worker = get_object_or_404(Worker, phone=phone)
        serializer = self.serializer(worker)
        return Response(serializer.data)


class WorkerVisitView(APIView):
    serializer = VisitSerializer

    def post(self, request, format=None):
        phone = request.data.get('phone')
        message = get_phone(phone)
        if message:
            return Response(message)
        worker = get_object_or_404(Worker, phone=phone)

        pk = request.data.get('pk')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        if not pk or not latitude or not longitude:
            return Response('Provide all three fields, (pk,latitude,longitude)!')
        if int(pk) not in list(worker.stores.all().values_list('id', flat=True)):
            return Response('The worker does not belong to the outlet!')

        store = get_object_or_404(Store, id=pk)
        visit = Visit.objects.create(store=store, latitude=latitude, longitude=longitude)
        serializer = self.serializer(visit)
        return Response(serializer.data)
