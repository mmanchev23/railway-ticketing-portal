from utils.passenger import Passenger
from utils.system import System


def main() -> None:
    system = System()

    # Case 1: Rush Hour, Adult, No Card
    # Ticket time: "08:00", Age: 30, Card: None, RoundTrip: False
    p1 = Passenger(30, None)
    price1 = system.calculate_price("08:00", p1.age, p1.rail_card_type, False)
    print(f"Rush Hour Adult: {price1} EUR (Expected: 100.0)")

    # Case 2: Saver Time, Adult, No Card
    # Ticket time: "11:00", Age: 30, Card: None, RoundTrip: False
    p2 = Passenger(30, None)
    price2 = system.calculate_price("11:00", p2.age, p2.rail_card_type, False)
    print(f"Saver Adult:     {price2} EUR (Expected: 95.0)")

    # Case 3: Saver Time, Senior Card
    # Ticket time: "11:00", Age: 65, Card: "Senior", RoundTrip: False
    p3 = Passenger(65, "Senior")
    price3 = system.calculate_price("11:00", p3.age, p3.rail_card_type, False)
    print(f"Saver Senior:    {price3} EUR (Expected: 62.7)")

    # Case 4: Rush Hour, Child with Family Card
    # Ticket time: "08:00", Age: 10, Card: "Family", RoundTrip: False
    p4 = Passenger(10, "Family")
    price4 = system.calculate_price("08:00", p4.age, p4.rail_card_type, False)
    print(f"Rush Hour Child: {price4} EUR (Expected: 50.0)")


if __name__ == "__main__":
    main()
