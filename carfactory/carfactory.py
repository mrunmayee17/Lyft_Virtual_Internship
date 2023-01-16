from battery.batterytypes.nubbinbattery import NubbinBattery
from battery.batterytypes.splinderbattery import SpindlerBattery
from battery.battery import Battery
from engine.enginetypes.capuletengine import CapuletEngine
from engine.enginetypes.sternmanengine import SternmanEngine
from engine.enginetypes.wiloughbyengine import WilloughbyEngine
from tire.tiretypes.carrigantire import CarriganTires
from tire.tiretypes.octoprimetire import OctoprimeTires
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date,last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery)
        return car
    @staticmethod
    def create_glissade(current_date,last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTires(tire_wear)
        car = Car(engine, battery)
        return car
    @staticmethod
    def create_palindrome(current_date,last_service_date, warning_light_is_on, tire_wear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery)
        return car
    @staticmethod
    def create_rorschach(current_date,last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine, battery)
        return car
    @staticmethod
    def create_thovex(current_date,last_service_date, current_mileage, last_service_mileage, tire_wear ):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery)
        return car