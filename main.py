class Flight:
    def __init__(self, fid, route):
        self.fid = fid
        self.route = route
        self.seats = 50


class Passenger:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name


class Airline:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.fid] = flight

    def book(self, fid):
        if fid in self.flights and self.flights[fid].seats > 0:
            self.flights[fid].seats -= 1
