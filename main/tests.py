from django.test import TestCase
from .models import ToDoList

# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.list = ToDoList.objects.create(name="fjeo")

    def test_todolist_model(self):
        l = self.list
        self.assertTrue(isinstance(l, ToDoList))
        self.assertEquals(str(l), "fjeo")
