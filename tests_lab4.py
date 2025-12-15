import unittest

from utils.system import System


class TestRailwayPricing(unittest.TestCase):
    def setUp(self) -> None:
        """Initialize the System before each test"""
        self.system = System()

    # ==========================================
    # 1. Statement Coverage (SC) Tests
    # Goal: Execute every line of code at least once
    # ==========================================
    def test_sc01_rush_senior_roundtrip(self) -> None:
        """Path: Rush Hour -> Senior Discount -> Round Trip"""
        # Input: 08:00 (Rush), Age 65 (Senior), RoundTrip=True
        # Calc: 100 * 1.0 (Rush) * 0.66 (Senior) * 2 (RoundTrip) = 132.0
        price = self.system.calculate_price("08:00", 65, "Senior", True)
        self.assertEqual(price, 132.0)

    def test_sc02_saver_family_child_oneway(self) -> None:
        """Path: Saver -> Child -> Family -> One Way"""
        # Input: 11:00 (Saver), Age 10, Family Card, RoundTrip=False
        # Calc: 100 * 0.95 (Saver) * 0.50 (Family) = 47.5
        price = self.system.calculate_price("11:00", 10, "Family", False)
        self.assertEqual(price, 47.5)

    def test_sc03_saver_std_child_oneway(self) -> None:
        """Path: Saver -> Child -> No Family -> One Way"""
        # Input: 11:00 (Saver), Age 10, No Card, RoundTrip=False
        # Calc: 100 * 0.95 (Saver) * 0.90 (Std Child) = 85.5
        price = self.system.calculate_price("11:00", 10, None, False)
        self.assertEqual(price, 85.5)

    # ==========================================
    # 2. Decision/Condition Coverage Tests
    # Goal: Test Edge cases for Time and Logic boundaries
    # ==========================================
    def test_cc01_exact_rush_start(self) -> None:
        """Boundary: Exactly 16:00 (Should be Rush Hour)"""
        # Calc: 100 * 1.0 * 1.0 = 100.0
        price = self.system.calculate_price("16:00", 30, None, False)
        self.assertEqual(price, 100.0)

    def test_cc02_exact_rush_end(self) -> None:
        """Boundary: Exactly 19:30 (Should be Rush Hour)"""
        # Calc: 100 * 1.0 * 1.0 = 100.0
        price = self.system.calculate_price("19:30", 30, None, False)
        self.assertEqual(price, 100.0)

    def test_cc03_just_after_rush(self) -> None:
        """Boundary: 19:31 (Should be Saver)"""
        # Calc: 100 * 0.95 * 1.0 = 95.0
        price = self.system.calculate_price("19:31", 30, None, False)
        self.assertEqual(price, 95.0)

    def test_cc04_senior_age_boundary(self) -> None:
        """Boundary: Age 59 (Not Senior) vs 60 (Senior)"""
        # Age 59: No discount (100.0) - Assuming Rush Hour
        price_59 = self.system.calculate_price("08:00", 59, "Senior", False)
        self.assertEqual(price_59, 100.0)

        # Age 60: Senior Discount (66.0)
        price_60 = self.system.calculate_price("08:00", 60, "Senior", False)
        self.assertEqual(price_60, 66.0)


if __name__ == "__main__":
    unittest.main()
