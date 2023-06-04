from rest_framework import viewsets

from authorize.models import Person
from bm_api.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

