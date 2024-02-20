from collections import deque

amount_of_money_in_pocket = [int(x) for x in input().split()]
prices_of_foods = deque(int(x) for x in input().split())

bought_food = 0

while amount_of_money_in_pocket and prices_of_foods:
    amount_of_money = amount_of_money_in_pocket.pop()
    price = prices_of_foods.popleft()

    if amount_of_money == price:
        bought_food += 1

    elif amount_of_money > price:
        bought_food += 1
        difference = amount_of_money - price

        if amount_of_money_in_pocket:
            amount_of_money_in_pocket[-1] += difference

if bought_food >= 4:
    print(f"Gluttony of the day! Henry ate {bought_food} foods.")
elif 1 < bought_food < 4:
    print(f"Henry ate: {bought_food} foods.")
elif bought_food == 1:
    print(f"Henry ate: {bought_food} food.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")