"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    """Adds new item to basket and groups identical items"""
    item_name = item["name"]
    item_price = item["price"]

    for basket_item in basket:
        if basket_item["name"] == item_name and basket_item["price"] == item_price:
            basket_item["count"] += 1
            return basket

    basket.append({
        "name": item_name,
        "price": item_price,
        "count": 1
    })
    return basket


def generate_receipt(basket: list) -> str:
    total = 0
    receipt = ""
    if basket == []:
        return ("Basket is empty")

    for item in basket:
        name = item["name"]
        price = item["price"]
        quantity = item["count"]

        line_total = price * quantity
        total += line_total

        if price == 0:
            line = f"{name} x {quantity} - Free\n"
        else:
            line = f"{name} x {quantity} - £{line_total:.2f}\n"

        receipt += line

    receipt += f"Total: £{total:.2f}"
    return receipt  # return the receipt string


#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
