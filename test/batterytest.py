import unittest
from datetime import datetime
from battery.batterytypes.nubbinbattery import NubbinBattery
from battery.batterytypes.splinderbattery import SpindlerBattery
from battery.battery import Battery
class TestNubbinBattery(unittest.TestCase):
    def nubbin_needs_service_true(self):
        current_date = datetime.datetime(2023, 5, 22)
        last_service_date = datetime.datetime(2018,1,22)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def nubbin_needs_service_false(self):
        current_date = datetime.datetime(2023, 9, 17)
        last_service_date = datetime.datetime(2016,4,19)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSplinderBattery(unittest.TestCase):
    def splinder_needs_service_true(self):
        current_date = datetime.datetime(2023, 5, 22)
        last_service_date = datetime.datetime(2018,1,22)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def splinder_needs_service_false(self):
        current_date = datetime.datetime(2023, 9, 17)
        last_service_date = datetime.datetime(2016,4,19)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())