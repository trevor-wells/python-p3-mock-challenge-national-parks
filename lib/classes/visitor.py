class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15 and not hasattr(self, 'name'):
            self._name = new_name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips

    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark):
            self._national_parks.append(new_national_park)
        return self._national_parks