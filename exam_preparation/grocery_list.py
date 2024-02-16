def shop_from_grocery_list(budget, gros_list, *products_and_prices):
    bought_groceries = []

    for product, price in products_and_prices:
        if product in gros_list and budget >= price and product not in bought_groceries:
            bought_groceries.append(product)
            gros_list.remove(product)
            budget -= price

        if budget < price:
            break

    if not gros_list:
        return(f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        return(f"You did not buy all the products. Missing products: {', '.join(str(x) for x in gros_list)}.")

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))