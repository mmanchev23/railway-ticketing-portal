import unittest

from utils.system import System


class TestFunctionalLab6(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

    def test_bva_time_boundaries(self) -> None:
        """Test exact boundary times for Rush Hour vs Saver"""
        p1 = self.system.calculate_price("09:29", 30, None, False)
        self.assertEqual(p1, 100.0, "09:29 should be Rush Hour")

        p2 = self.system.calculate_price("09:30", 30, None, False)
        self.assertEqual(p2, 95.0, "09:30 should be Saver")

    def test_bva_age_boundaries(self) -> None:
        """Test exact age boundary for Child vs Adult"""
        # 100 * 1.0 (Rush) * 0.90 = 90.0
        p_child = self.system.calculate_price("08:00", 15, None, False)
        self.assertEqual(p_child, 90.0)

        p_adult = self.system.calculate_price("08:00", 16, None, False)
        self.assertEqual(p_adult, 100.0)

    def test_ecp_valid_classes(self) -> None:
        """Test representative values from valid classes"""
        # 100 * 0.95 * 0.66 = 62.7
        p_senior = self.system.calculate_price("11:00", 65, "Senior", False)
        self.assertEqual(p_senior, 62.7)

        # 100 * 1.0 * 0.50 = 50.0
        p_family = self.system.calculate_price("08:00", 10, "Family", False)
        self.assertEqual(p_family, 50.0)

    def test_decision_table_combinations(self) -> None:
        """Test specific rule combinations"""
        # Rule: Rush Hour + Senior + Senior Card = 0.66
        p = self.system.calculate_price("08:00", 70, "Senior", False)
        self.assertEqual(p, 66.0)

    def test_state_transitions(self) -> None:
        """Test Reservation lifecycle: Create -> Cancel"""
        self.system.create_profile("u100", "Alice", "alice@test.com")
        res = self.system.create_reservation("u100", "T1", 100.0)
        self.assertEqual(res.status, "CONFIRMED")
        self.system.cancel_reservation(res.res_id)
        self.assertEqual(res.status, "CANCELLED")


if __name__ == "__main__":
    unittest.main()
