yearly_fee = int(input())

price_shoes = yearly_fee - (yearly_fee * 0.4)
price_uniform = price_shoes - (price_shoes * 0.2)
price_ball = price_uniform * 0.25
price_accessories = price_ball * 0.2
total_price = yearly_fee + price_shoes + price_uniform + price_ball + price_accessories

print(total_price)
