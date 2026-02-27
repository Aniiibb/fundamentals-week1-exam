"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    """Function changes the receipt into an invoice"""
    if receipt_string == "" or receipt_string == "Total: £0.00":
        return ("VAT RECEIPT\n\nTotal: £0.00\nVAT: £0.00\nTotal inc VAT: £0.00")

    receipt_split = receipt_string.split("\n")

    invoice = "VAT RECEIPT\n\n"
    line_for_total = ""
    for line in receipt_split:
        if line[:5] == "Total":
            line_for_total += line
            break
    list_of_prices = []
    for line in receipt_split:
        price_without_tax = float(line[-4:]) * 0.8
        list_of_prices.append(price_without_tax)
        if line[:5] == "Total":
            line_for_total += line
            break

    print(f"{price_without_tax:.2f}")
    return invoice  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
