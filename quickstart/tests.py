import unittest
import uuid
from django.test import Client
from django.core.urlresolvers import reverse
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from quickstart.models import Person
from quickstart.serializers import PersonSerializer


def create_person(**kwargs):
    defaults = {}
    defaults["name"] = uuid.uuid4()
    defaults.update(**kwargs)
    return Person.objects.create(**defaults)


class PersonAPITest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_person(self):
        url = reverse('person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_person(self):
        url = reverse('person_list')
        data = {
            "name": str(uuid.uuid4())
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)

    def test_detail_person(self):
        person = create_person()
        url = reverse('person_detail', args=[person.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_person(self):
        person = create_person()
        data = {
            "name": str(uuid.uuid4())
        }
        url = reverse('person_detail', args=[person.pk, ])
        serialized = json.dumps(data)
        response = self.client.put(
            url, serialized, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_delete_person(self):
        person = create_person()
        url = reverse('person_detail', args=[person.pk, ])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


'''
requests

#list:   http http://127.0.0.1:8000/person/
#detail: http http://127.0.0.1:8000/person/1/
#insert: http POST http://127.0.0.1:8000/person/ name='jesus'
#update: http PUT http://127.0.0.1:8000/person/2/ name='ana'
#delete: http DELETE http://127.0.0.1:8000/person/2/



http http://127.0.0.1:8000/person/ Accept:application/json
or
http http://127.0.0.1:8000/person.json

http http://127.0.0.1:8000/person/ Accept:text/html
or
http http://127.0.0.1:8000/person.api


with forms
http --form POST http://127.0.0.1:8000/person/ name="dorii"
'''
