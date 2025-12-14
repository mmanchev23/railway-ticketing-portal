from datetime import datetime


class Reservation:
    def __init__(self, res_id, user_profile, ticket_details, price) -> None:
        self.res_id = res_id
        self.user_profile = user_profile
        self.ticket_details = ticket_details
        self.price = price
        self.status = "CONFIRMED"
        self.created_at = datetime.now()

    def cancel(self) -> None:
        self.status = "CANCELLED"

    def modify(self, new_ticket_details, new_price) -> None:
        self.ticket_details = new_ticket_details
        self.price = new_price
        self.status = "MODIFIED"

    def __str__(self) -> str:
        return f"[ID: {self.res_id}] Status: {self.status} | Price: {self.price} EUR"
