from dateutil import parser, tz
from django.test import TestCase
from freezegun import freeze_time
from ninja.testing import TestClient
import datetime

from difference.api import router


class TestDifference(TestCase):
    def setUp(self):
        self.test_client = TestClient(router)

    def test_difference_math(self):
        start_date = datetime.datetime(
            year=2025, month=6, day=9, hour=13, minute=20, second=15, tzinfo=tz.UTC
        )
        with freeze_time(start_date):
            response = self.test_client.get("/difference?number=10")

            self.assertEqual(response.status_code, 200)

            json_data = response.json()
            self.assertIn("value", json_data)
            self.assertEqual(json_data["value"], 2640)
            self.assertIn("number", json_data)
            self.assertEqual(json_data["number"], 10)
            self.assertIn("datetime", json_data)
            self.assertEqual(parser.parse(json_data["datetime"]), start_date)
            self.assertIn("last_datetime", json_data)
            self.assertEqual(json_data["last_datetime"], None)
            self.assertIn("occurences", json_data)
            self.assertEqual(json_data["occurences"], 1)

        # change date and request again
        # Testing that occurences is incremented, datetime changes, and last_datetime equals the previous datetime
        end_date = datetime.datetime(
            year=2025, month=6, day=9, hour=14, minute=20, second=15, tzinfo=tz.UTC
        )
        with freeze_time(end_date):
            response = self.test_client.get("/difference?number=10")

            self.assertEqual(response.status_code, 200)

            json_data = response.json()
            self.assertIn("value", json_data)
            self.assertEqual(json_data["value"], 2640)
            self.assertIn("number", json_data)
            self.assertEqual(json_data["number"], 10)
            self.assertIn("datetime", json_data)
            self.assertEqual(parser.parse(json_data["datetime"]), end_date)
            self.assertIn("last_datetime", json_data)
            self.assertEqual(parser.parse(json_data["last_datetime"]), start_date)
            self.assertIn("occurences", json_data)
            self.assertEqual(json_data["occurences"], 2)

    def test_difference_range_error(self):
        response = self.test_client.get("/difference?number=101")
        self.assertEqual(response.status_code, 422)
        json_data = response.json()
        self.assertEqual(
            json_data["message"],
            "Value for 'number' too large, must be <= 100",
        )

        response = self.test_client.get("/difference?number=0")
        self.assertEqual(response.status_code, 422)
        json_data = response.json()
        self.assertEqual(
            json_data["message"],
            "Value for 'number' too small, must be > 0",
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
