from .passenger import Passenger
from .ticket import Ticket


class System:
    def calculate_final_price(self, ticket: Ticket, passenger: Passenger) -> float:
        time_multiplier = ticket.get_time_multiplier()
        price_after_time = ticket.base_price * time_multiplier

        passenger_multiplier = passenger.get_discount_multiplier()

        final_price = price_after_time * passenger_multiplier
        return round(final_price, 2)
