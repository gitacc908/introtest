from rest_framework import serializers
from .models import Worker, Store, Visit


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['name', 'worker']


class WorkerSerializer(serializers.ModelSerializer):
    stores = StoreSerializer(many=True)
    class Meta:
        model = Worker
        fields = ['id', 'name', 'stores']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'date']
