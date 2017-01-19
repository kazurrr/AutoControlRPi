import json
from subprocess import call


class Position:
    cmd_get_position = "gpspipe -w -n 30 | grep -m 1 lat | jq '.'"

    def __init__(self):
        pass

    def get_current_position(self):
        response = call(self.cmd_get_position)
        gps_data = json.loads(response)

        return LatLon(lat=gps_data["lat"], lon=gps_data["lon"])


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon
