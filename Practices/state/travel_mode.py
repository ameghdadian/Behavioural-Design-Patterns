from abc import ABC, abstractmethod

class TravelMode(ABC):
    @abstractmethod
    def calc_eta(self):
        pass

    @abstractmethod
    def calc_direction(self):
        pass


class Driving(TravelMode):
    def calc_eta(self):
        print("Calculating ETA (driving)")

    def calc_direction(self):
        print("Calculating Direction (driving)")


class Bicycling(TravelMode):
    def calc_eta(self):
        print("Calculating ETA (bicycling)")

    def calc_direction(self):
        print("Calculating Direction (bicycling)")


class Transit(TravelMode):
    def calc_eta(self):
        print("Calculating ETA (transit)")

    def calc_direction(self):
        print("Calculating Direction (transit)")


class Walking(TravelMode):
    def calc_eta(self):
        print("Calculating ETA (walking)")

    def calc_direction(self):
        print("Calculating Direction (walking)")
