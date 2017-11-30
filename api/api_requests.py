import requests
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class VehicleStopsRequests():
    def __init__(self, endpoint, headers):
        self.endpoint = endpoint
        self.headers = headers

    def get_vehicle_stops_page(self, page=1):
        r = requests.get(self.endpoint + '?page=' + str(page), headers = self.headers)
        if r.status_code == 200:
            return r.text
        else:
            return r


if __name__ == "__main__":
    endpoint = "http://127.0.0.1:5000/vehicle_stops/v0.1"
    headers = {'Content-Type': 'application/json'}
    # Example payload...
    # payload = {'key':'my-key', 'token': 'my-token'}
    v = VehicleStopsRequests(endpoint, headers)
    try:
        vehicle_stops_list = v.get_vehicle_stops_page()
        print(vehicle_stops_list)
    except requests.exceptions.ConnectionError as ce:
        log.error("Connection error - check if endpoint is correct and service is running.")
        log.error(ce)