import sys

from utils.system import System


def print_menu() -> None:
    print("\n--- Railway Ticketing System ---")
    print("1. Create User Profile")
    print("2. Search for Trains")
    print("3. Book a Ticket")
    print("4. View My Reservations")
    print("5. Cancel a Reservation")
    print("6. Admin: Run Pricing Test")
    print("7. Exit")
    print("---------------------------------")


def main() -> None:
    system = System()

    try:
        system.create_profile("u1", "John Doe", "john@example.com")
        system.create_profile("u2", "Jane Smith", "jane@example.com")
    except ValueError:
        pass

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            uid = input("Enter User ID (e.g., u100): ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")

            try:
                user = system.create_profile(uid, name, email)
                print(f"Success! Created profile: {user}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            print("\nAvailable Destinations: Paris, London")
            dest = input("Enter Destination: ")
            time_str = input("Enter Departure Time (HH:MM): ")
            found = False

            from utils.system import TRAINS_DB

            print(f"\n--- Search Results for {dest} after {time_str} ---")

            for t in TRAINS_DB:
                if t["dest"].lower() == dest.lower() and t["time"] >= time_str:
                    print(f"Train {t['id']} to {t['dest']} at {t['time']}")
                    found = True

            if not found:
                print("No trains found.")

        elif choice == "3":
            print("\n--- Book a Ticket ---")
            user_id = input("Enter User ID: ")
            user = system.get_profile(user_id)

            if not user:
                print("User not found. Please create a profile first.")
                continue

            train_id = input("Enter Train ID (e.g., T1): ")
            time_str = input("Enter Departure Time (HH:MM): ")

            try:
                age = int(input("Enter Passenger Age: "))
            except ValueError:
                print("Invalid age.")
                continue

            card = input("Enter Rail Card (Senior/Family/None): ")
            if card.lower() == "none" or card == "":
                card = None

            trip_type = input("Round Trip? (y/n): ").lower()
            is_round = trip_type == "y"

            coupon = input("Enter Coupon Code (optional): ")
            if coupon == "":
                coupon = None

            try:
                price = system.calculate_price(time_str, age, card, is_round, coupon)
                print(f"\nCalculated Price: {price} EUR")

                confirm = input("Confirm Booking? (y/n): ").lower()
                if confirm == "y":
                    res = system.create_reservation(user_id, train_id, price)
                    print(f"Booking Confirmed! Reservation ID: {res.res_id}")
                else:
                    print("Booking cancelled by user.")

            except Exception as e:
                print(f"Error calculating price: {e}")

        elif choice == "4":
            user_id = input("Enter User ID: ")
            user = system.get_profile(user_id)

            if user:
                print(f"\n--- Reservations for {user.name} ---")
                if not user.reservations:
                    print("No reservations found.")
                for res in user.reservations:
                    print(res)
            else:
                print("User not found.")

        elif choice == "5":
            try:
                res_id = int(input("Enter Reservation ID to cancel: "))
                success = system.cancel_reservation(res_id)

                if success:
                    print(f"Reservation {res_id} has been CANCELLED.")
                else:
                    print("Reservation ID not found.")
            except ValueError:
                print("Invalid ID format.")

        elif choice == "6":
            print("\n--- Running Pricing Smoke Test ---")
            p = system.calculate_price("08:00", 30, None, False)
            print(f"Rush Hour Adult: {p} EUR (Expected: 100.0)")
            p2 = system.calculate_price("11:00", 65, "Senior", False)
            print(f"Saver Senior: {p2} EUR (Expected: 62.7)")

        elif choice == "7":
            print("Exiting ... Safe travels!")
            sys.exit()

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
