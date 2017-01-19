import json
import urllib2

import time

from auto_control_pi.car_data import CarData
from auto_control_pi.config import Config
from auto_control_pi.position import Position


class MainProgram:
    def __init__(self):
        self.gps = Position()
        self.can = CarData()
        self.sending_details = True
        self.refresh_rate_in_second = 10

    def start_broadcasting(self):
        self.sending_details = True

        while self.sending_details:
            self.send_data()
            time.sleep(self.refresh_rate_in_second)

    def stop_broadcasting(self):
        self.sending_details = False

    def send_data(self):
        data = self.collect_data()

        req = urllib2.Request(Config.detail_url)
        req.add_header('Content-Type', 'application/json')

        urllib2.urlopen(req, json.dumps(data))

    def collect_data(self):
        position = self.gps.get_current_position()

        return {
            "CarId": 1,
            "Speed": self.can.get_speed(),
            "Rpm": self.can.get_rpm(),
            "EngineLoad": self.can.get_engine_load(),
            "Voltage": self.can.get_voltage(),
            "Lat": position.get_lat(),
            "Lon": position.get_lon()
        }


MainProgram().start_broadcasting()
