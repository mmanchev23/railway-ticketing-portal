from utils.system import System


def main() -> None:
    sys = System()

    # 1. Test Refactored Pricing (Should still work same as Lab 4)
    price = sys.calculate_price("08:00", 30, None, False)
    print(f"Standard Rush Price: {price} (Expected: 100.0)")

    # 2. Test Coupon Feature
    price_coupon = sys.calculate_price("08:00", 30, None, False, coupon_code="SUMMER20")
    print(f"Price with SUMMER20 Coupon: {price_coupon} (Expected: 80.0)")

    # 3. Test Profile Creation
    user = sys.create_profile("u001", "John Doe", "john@example.com")
    print(f"Profile Created: {user}")

    # 4. Test Reservation
    res = sys.create_reservation("u001", "T1", price_coupon)
    print(f"Reservation Created: {res}")

    # 5. Cancel Reservation
    sys.cancel_reservation(res.res_id)
    print(f"Reservation Status after Cancel: {res.status}")


if __name__ == "__main__":
    main()
