# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

class SomeTestCase(TestCase):
	fixtures = ["test0.json"]
	def test_func(self):
		response = self.client.get(reverse("run"))
		self.failUnlessEqual(response.status_code, 200)
		response = self.client.get(reverse("my"), {"my": "model2"})
		self.failUnlessEqual(response.status_code, 200)
		response = self.client.get(reverse("insert"), {'my': 'model2_Kom_123'})
		self.failUnlessEqual(response.status_code, 200)
		response = self.client.get(reverse("run"))
		self.failUnlessEqual(response.status_code, 200)
		response = self.client.get(reverse("run"))
		self.failUnlessEqual(response.status_code, 200)
		response = self.client.get(reverse("update"), {'my': '_model2_2_1_privet'})
		self.failUnlessEqual(response.status_code, 200)
		response = self.client.get(reverse("run"))
		self.failUnlessEqual(response.status_code, 200)
