DISCOUNT_SENIOR = 0.66
DISCOUNT_FAMILY_CHILD = 0.50
DISCOUNT_CHILD_STD = 0.90


class Passenger:
    def __init__(self, age: int, rail_card_type: str = None) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative")  # (DEF-003)

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
            return DISCOUNT_SENIOR

        if self.age < 16:
            if self.rail_card_type == "Family":
                return DISCOUNT_FAMILY_CHILD
            else:
                return DISCOUNT_CHILD_STD

        return 1.0
