from datetime import datetime, time


BASE_FARE = 100.0
RUSH_START_AM = time(9, 30)
RUSH_START_PM = time(16, 0)
RUSH_END_PM = time(19, 30)


TRAINS_DB = [
    {"id": "T1", "dest": "Paris", "time": "08:00"},
    {"id": "T2", "dest": "Paris", "time": "11:00"},
    {"id": "T3", "dest": "London", "time": "17:00"},
]


class System:
    def search_trains(self, destination, dep_time_str) -> list[dict]:
        """Simple search module"""
        results = []

        for t in TRAINS_DB:
            if t["dest"] == destination:
                if t["time"] >= dep_time_str:
                    results.append(t)

        return results

    def calculate_price(self, dep_time_str, age, card_type, is_round_trip) -> float:
        """
        The Core Function we will use for White Box Testing.
        Calculates price based on Time, Age, Card, and Trip Type.
        """
        price = BASE_FARE
        t = datetime.strptime(dep_time_str, "%H:%M").time()
        is_rush_hour = (t < RUSH_START_AM) or (RUSH_START_PM <= t <= RUSH_END_PM)

        if is_rush_hour:
            multiplier = 1.0
        else:
            multiplier = 0.95

        price = price * multiplier

        if age >= 60 and card_type == "Senior":
            price = price * 0.66
        elif age < 16:
            if card_type == "Family":
                price = price * 0.50
            else:
                price = price * 0.90

        if is_round_trip:
            price = price * 2

        return round(price, 2)

    def book_ticket(self, train_id, price) -> str:
        return f"Ticket booked for {train_id} at {price} EUR"
