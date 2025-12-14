from utils.passenger import Passenger
from utils.system import System
from utils.ticket import Ticket


def main() -> None:
    system = System()

    # Case 1: Rush Hour, Adult, No Card
    # Expected: 100.0
    t1 = Ticket(100.0, "08:00")
    p1 = Passenger(30, None)
    print(f"Rush Hour Adult: {system.calculate_final_price(t1, p1)}")

    # Case 2: Saver Time, Adult, No Card
    # Expected: 95.0
    t2 = Ticket(100.0, "11:00")
    p2 = Passenger(30, None)
    print(f"Saver Adult: {system.calculate_final_price(t2, p2)}")

    # Case 3: Saver Time, Senior Card
    # Expected: 95 * 0.66 = 62.7
    t_senior = Ticket(100.0, "11:00")
    p_senior = Passenger(65, "Senior")
    print(f"Saver Senior: {system.calculate_final_price(t_senior, p_senior)}")

    # Case 4: Rush Hour, Child with Family Card
    # Expected: 100 * 0.5 = 50.0
    t_child = Ticket(100.0, "08:00")
    p_child = Passenger(10, "Family")
    print(f"Rush Hour Child (Family): {system.calculate_final_price(t_child, p_child)}")


if __name__ == "__main__":
    main()
