import unittest
from datetime import datetime
from engine.enginetypes.capuletengine import CapuletEngine
from engine.enginetypes.sternmanengine import SternmanEngine
from engine.enginetypes.wiloughbyengine import WilloughbyEngine

class CapuletTestEngine:
    def capulet_needs_service_true(self):
        current_mileage = 67031
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    def capulet_needs_service_false(self):
        current_mileage = 60019
        last_service_mileage = 20
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class WilloughbyTestEngine:   
    def willoughby_needs_service_true(self):
        current_mileage = 67031
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    def willoughby_needs_service_false(self):
        current_mileage = 60019
        last_service_mileage = 20
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class SternmanTestEngine:
    def sternman_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def sternman_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
