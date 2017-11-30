import unittest
import mock
from mock import Mock
import api.api_requests as req

VEHICLE_STOPS_ENDPOINT = "http://127.0.0.1:5000/vehicle_stops/v0.1"
sample_page_1_results = """{
                                  "stop": [
                                    {
                                      "service_area": 101,
                                      "stop_cause": "Equipment Violation",
                                      "stop_id": 123456,
                                      "subject_race": "H"
                                    },
                                    {
                                      "service_area": 102,
                                      "stop_cause": "Moving Violation",
                                      "stop_id": 123457,
                                      "subject_race": "W"
                                    }
                                  ]
                                 }
                              """


class TestApiRequests(unittest.TestCase):
    def setUp(self):
        self.sample_text = sample_page_1_results
        self.vehicle_stops_request = req.VehicleStopsRequests(VEHICLE_STOPS_ENDPOINT, {'Content-Type': 'application/json'})

    def mocked_requests_get(*args, **kwargs):
        class MockVehicleStops():
            def __init__(self, data, status_code):
                self.json_data = data
                self.text = data
                self.status_code = status_code

                def json(self):
                    return self.json_data

                def text(self):
                    return self._text

                def status_code(self):
                    return self.status_code

        sample_text = sample_page_1_results
        if args[0] == VEHICLE_STOPS_ENDPOINT + '?page=1':
            return MockVehicleStops(sample_text, 200)
        return MockVehicleStops(sample_text, 200)