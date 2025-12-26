class Airport:

    def __init__(self, name):
        self.name = name
        self.flights = []           # list available flights
        self.passenger_queue = []   # passenger queue

    def add_flight(self, flight):
        self.flights.append(flight)

    def enqueue_passenger(self, passenger):
        self.passenger_queue.append(passenger)

    def dequeue_passenger(self):
        if not self.passenger_queue:
            return None
        return self.passenger_queue.pop(0)

    def security_check(self, passenger):
        if not passenger.has_passport:
            return f"{passenger.name}: Passport missing."
        if passenger.heavy_bag:
            return f"{passenger.name}: Extra fee required."
        if passenger.delay_flight:
            return f"{passenger.name}: Please wait in the lounge."
        return f"{passenger.name}: Cleared for boarding."
