original_price_and_discount = input().strip()

original_price, discount = map(float, original_price_and_discount.split())

if 0 <= original_price <= 100000 and 0 <= discount <= 100000:

    discount_amount = (original_price * discount) / 100
    final_result = original_price - discount_amount

    print(f"price: {final_result:.2f}")
else:
    pass
