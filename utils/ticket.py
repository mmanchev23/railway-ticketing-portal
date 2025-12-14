from datetime import datetime, time


RUSH_HOUR_START_1 = time(9, 30)
RUSH_HOUR_START_2 = time(16, 0)
RUSH_HOUR_END_2 = time(19, 30)
DISCOUNT_SAVER = 0.95


class Ticket:
    def __init__(self, base_price: float, departure_time: str) -> None:
        self.base_price = base_price

        try:
            self.time_obj = datetime.strptime(
                departure_time, "%H:%M"
            ).time()  # (DEF-002)
        except ValueError:
            raise ValueError("Time must be in HH:MM format")

    def get_time_multiplier(self) -> float:
        """
        Logic:
        - Rush Hour: < 9:30 OR 16:00-19:30 -> Full Fare (1.0)
        - Saver: 9:30-16:00 OR > 19:30 -> 5% Discount (0.95)
        """
        t = self.time_obj

        if t < RUSH_HOUR_START_1:
            return 1.0
        elif RUSH_HOUR_START_2 <= t <= RUSH_HOUR_END_2:
            return 1.0
        else:
            return DISCOUNT_SAVER
