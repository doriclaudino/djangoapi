from rest_framework import mixins
from rest_framework import generics
from quickstart.models import Person
from quickstart.serializers import PersonSerializer


class PersonList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    List all persons, or create a new person.
        RetrieveModelMixin .list()
        CreateModelMixin   .perform_create()
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PersonDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    """
    Retrieve, update or delete a person instance.
        RetrieveModelMixin .retrieve()
        UpdateModelMixin   .perform_update()
        DestroyModelMixin  .perform_destroy()
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
