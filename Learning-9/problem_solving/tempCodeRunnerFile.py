p = int(input())
dis = int(input())

price = float(p)
discount = float(dis)

discounted_price = price - (price * discount / 100)

print(f"price: {discounted_price:.2f}")
