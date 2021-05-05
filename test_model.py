from django.test import TestCase
from .models import Files

class FilesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Files.objects.create(descr="2.txt description",filename="2.txt")

    def test_getFileDescription(self):
        file = Files.objects.get(filename="2.txt")
        self.assertEquals(Files.getDescription(),'2.txt description')
