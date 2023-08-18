from django.test import TestCase

from mraiyastore.models import Category, Product

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='fashion', slug='fashion')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))