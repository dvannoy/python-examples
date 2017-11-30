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


    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_successful_get_vehicle_stops_page(self, mock_get):
        res = self.vehicle_stops_request.get_vehicle_stops_page()
        self.assertEquals(res,self.sample_text)