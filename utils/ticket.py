from datetime import datetime, time


class Ticket:
    def __init__(self, base_price: float, departure_time: str) -> None:
        self.base_price = base_price
        self.departure_time = departure_time
        self.time_obj = datetime.strptime(departure_time, "%H:%M").time()

    def get_time_multiplier(self) -> float:
        """
        Logic:
        - Rush Hour: < 9:30 OR 16:00-19:30 -> Full Fare (1.0)
        - Saver: 9:30-16:00 OR > 19:30 -> 5% Discount (0.95)
        """
        t = self.time_obj

        morning_rush_end = time(9, 30)
        afternoon_rush_start = time(16, 0)
        afternoon_rush_end = time(19, 30)

        if t < morning_rush_end:
            return 1.0
        elif afternoon_rush_start <= t <= afternoon_rush_end:
            return 1.0
        else:
            return 0.95
