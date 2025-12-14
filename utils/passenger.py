class Passenger:
    def __init__(self, age: int, rail_card_type: str = None) -> None:
        self.age = age
        self.rail_card_type = rail_card_type

    def get_discount_multiplier(self) -> float:
        """
        Logic:
        - Over 60s rail card: 34% discount (0.66 multiplier)
        - Child (< 16):
            - With Family Card: 50% discount (0.50 multiplier)
            - No Family Card: 10% discount (0.90 multiplier)
        """
        if self.rail_card_type == "Senior" and self.age >= 60:
            return 0.66

        if self.age < 16:
            if self.rail_card_type == "Family":
                return 0.50
            else:
                return 0.90

        return 1.0
