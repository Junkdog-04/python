class Customer:
    def __init__(self, name, has_passport=True, heavy_bag=False, delay_flight=False, seat_preference=None):
        self.name = name
        self.has_passport = has_passport
        self.heavy_bag = heavy_bag
        self.delay_flight = delay_flight

        # "window", "aisle" o None
        self.seat_preference = seat_preference

    def buy_ticket(self, flight_class):
        print(f"{self.name} bought a {flight_class} ticket.")

    def drive_to_airport(self):
        print(f"{self.name} is driving to the airport.")

    def register_bags(self):
        print(f"{self.name} registered baggage.")
