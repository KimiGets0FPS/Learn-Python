def profit_you_make(unit_cost, unit_sell, how_many):
    profit = unit_sell * how_many - unit_cost * how_many
    return profit


#            Cost to buy urself  sell price  amount
print(f"\nThe profit is {profit_you_make(30, 35, 100)}\n")
