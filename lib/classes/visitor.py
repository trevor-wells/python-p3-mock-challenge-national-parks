class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        pass

    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        pass