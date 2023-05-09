class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and not hasattr(self, 'name'):
            self._name = new_name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass 