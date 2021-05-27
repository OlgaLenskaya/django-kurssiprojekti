from django.http import response
from django.test import TestCase, Client, client
from .laskin import plus
from .models import Supplier, Product
from .views import supplierlistview, productlistview
import unittest
from django.urls import reverse
client = Client()

# palauttaa statuskoodin 200:
class ListMethodTesta(TestCase):
    def test_listing_products(self): 
        response = client.get(reverse(productlistview))
        self.assertEqual(response.status_code, 200)

class SupplierModelTests(TestCase):
    def setUp(self):
        Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", address="Kultatie 1", phone="123456", email="jaakko@kulta.fi", country="Finland")
    
    def test_added_supplier_exists(self):
        # Added supplier exists and can be searched
        supplier = Supplier.objects.get(companyname="Test company")
        self.assertEqual(supplier.address, "Kultatie 1")
        self.assertEqual(supplier.country, "Finland")
        
# class LaskinTests(TestCase):
#     def test_plus(self):
#         # testaa että numerot lasketaan yhteen oikein:
#         self.assertEqual(plus(7,2),9)

   

# @unittest. expectedFailure
# def test_plus_should_fail(self):
#     self.assertEqual(plus(7,3),10)
