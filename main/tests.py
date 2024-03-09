from django.test import TestCase
from .models import ToDoList


# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.list = ToDoList.objects.create(name="fjeo")

    def test_todolist_model(self):
        list_obj = self.list
        self.assertTrue(isinstance(list_obj, ToDoList))
        self.assertEquals(str(list_obj), "fjeo")
