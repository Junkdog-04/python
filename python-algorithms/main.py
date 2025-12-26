from customer import Customer
from airport import Airport
from flight import Flight

def main():
    airport = Airport("Mexico City International")
    flight = Flight("MX203", "Buenos Aires", "15:30", "boarding")
    airport.add_flight(flight)
    passengers = [
        Customer("Luis", seat_preference="window"),
        Customer("Ana", seat_preference="aisle", heavy_bag=True),
        Customer("Pedro", has_passport=False)
    ]
    for p in passengers:
        airport.enqueue_passenger(p)

    print("\n=== AIRPORT SIMULATION START ===")

    while True:
        passenger = airport.dequeue_passenger()
        if passenger is None:
            break

        print(f"\nProcessing passenger: {passenger.name}")


        sec = airport.security_check(passenger)
        print("Security:", sec)

        if "Cleared" not in sec:
            continue


        seat_msg = flight.assign_seat(passenger)
        print("Seat:", seat_msg)

        found_gate = flight.bfs_nearest_gate("Gate A", "Gate D")
        print("Gate path exists:", found_gate)

    print("\n=== END OF SIMULATION ===")


if __name__ == "__main__":
    main()
