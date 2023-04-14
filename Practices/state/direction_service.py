from travel_mode import TravelMode

class DirectionService:
    _travel_mode: TravelMode

    def get_eta(self):
        self.travel_mode.calc_eta()

    def get_direction(self):
        self.travel_mode.calc_direction()
    
    @property
    def travel_mode(self) -> TravelMode:
        return self._travel_mode
    
    @travel_mode.setter
    def travel_mode(self, mode):
        self._travel_mode = mode
