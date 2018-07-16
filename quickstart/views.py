from rest_framework import mixins
from rest_framework import generics
from quickstart.models import Person
from quickstart.serializers import PersonSerializer


class PersonList(generics.ListCreateAPIView):
    """
    List all persons, or create a new person.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a person instance.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
