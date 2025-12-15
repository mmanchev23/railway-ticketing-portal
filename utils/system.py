from datetime import datetime, time
from utils.reservation import Reservation
from utils.profile import UserProfile


BASE_FARE = 100.0
RUSH_START_AM = time(9, 30)
RUSH_START_PM = time(16, 0)
RUSH_END_PM = time(19, 30)

VALID_COUPONS = {
    "SUMMER20": 0.80,  # 20% off
    "WELCOME10": 0.90,  # 10% off
}

TRAINS_DB = [
    {"id": "T1", "dest": "Paris", "time": "08:00"},
    {"id": "T2", "dest": "Paris", "time": "11:00"},
    {"id": "T3", "dest": "London", "time": "17:00"},
]


class System:
    def __init__(self) -> None:
        self.users = {}
        self.reservations = {}
        self.res_counter = 1

    def create_profile(self, user_id, name, email) -> UserProfile:
        if user_id in self.users:
            raise ValueError("User ID already exists")
        user = UserProfile(user_id, name, email)
        self.users[user_id] = user
        return user

    def get_profile(self, user_id) -> UserProfile | None:
        return self.users.get(user_id)

    def create_reservation(self, user_id, train_id, price) -> Reservation:
        user = self.get_profile(user_id)

        if not user:
            raise ValueError("User not found")

        res_id = self.res_counter
        self.res_counter += 1

        train_details = next((t for t in TRAINS_DB if t["id"] == train_id), None)

        reservation = Reservation(res_id, user, train_details, price)
        self.reservations[res_id] = reservation
        user.reservations.append(reservation)
        return reservation

    def cancel_reservation(self, res_id) -> bool:
        if res_id in self.reservations:
            self.reservations[res_id].cancel()
            return True
        return False

    def _get_time_multiplier(self, time_obj) -> float:
        """Helper: logic for Rush Hour vs Saver"""
        is_rush_hour = (time_obj < RUSH_START_AM) or (
            RUSH_START_PM <= time_obj <= RUSH_END_PM
        )
        return 1.0 if is_rush_hour else 0.95

    def _get_passenger_multiplier(self, age, card_type) -> float:
        """Helper: logic for Age and Card discounts"""
        if age >= 60 and card_type == "Senior":
            return 0.66
        elif age < 16:
            if card_type == "Family":
                return 0.50
            else:
                return 0.90
        return 1.0

    def calculate_price(
        self, dep_time_str, age, card_type, is_round_trip, coupon_code=None
    ) -> float:
        """
        Refactored to use helper methods and support Coupons.
        """
        price = BASE_FARE
        t = datetime.strptime(dep_time_str, "%H:%M").time()

        price *= self._get_time_multiplier(t)

        price *= self._get_passenger_multiplier(age, card_type)

        if is_round_trip:
            price *= 2

        if coupon_code and coupon_code in VALID_COUPONS:
            price *= VALID_COUPONS[coupon_code]

        return round(price, 2)
