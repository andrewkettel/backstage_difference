from django.test import TestCase
from ninja.testing import TestClient

from .api import router


class TestDifference(TestCase):
    def setUp(self):
        self.test_client = TestClient(router)

    def test_difference_math(self):
        response = self.test_client.get("/difference?number=10")

        self.assertEqual(response.status_code, 200)

        json_data = response.json()
        self.assertIn("value", json_data)
        self.assertEqual(json_data["value"], 2640)
        self.assertIn("number", json_data)
        self.assertEqual(json_data["number"], 10)

    def test_difference_range_error(self):
        response = self.test_client.get("/difference?number=101")
        self.assertEqual(response.status_code, 422)
        json_data = response.json()
        self.assertEqual(
            json_data["message"],
            "Value for 'number' too large, must be <=100",
        )

    def test_difference_no_num(self):
        response = self.test_client.get("/difference")

        self.assertEqual(response.status_code, 422)
        json_data = response.json()
        self.assertEqual(
            json_data["detail"][0]["type"],
            "missing",
        )

    def test_difference_bad_value(self):
        response = self.test_client.get("/difference?number=hello")

        self.assertEqual(response.status_code, 422)
        json_data = response.json()
        self.assertEqual(
            json_data["detail"][0]["type"],
            "int_parsing",
        )
