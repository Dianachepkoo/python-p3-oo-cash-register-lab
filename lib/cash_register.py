class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = None  # Keep track of the last transaction

    def add_item(self, item_name, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.items.append({"item": item_name, "price": price, "quantity": quantity})
        self.last_transaction = item_cost  # Update last_transaction


    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            success_message = f"After the discount, the total comes to ${self.total:.2f}."
            return success_message
        else:
            return "No discount applied."


    def void_last_transaction(self):
        if self.last_transaction is not None:
            self.total -= self.last_transaction
            self.items.pop()  # Remove the last item from the list
            self.last_transaction = None
        else:
            return "No transactions to void."

# Example usage:
register = CashRegister(discount=10)
register.add_item("Apple", 1.5, quantity=3)
register.add_item("Banana", 0.75)
print(register.total)  # Total without discount
print(register.apply_discount())  # Apply discount if applicable
print(register.total)  # Total after discount
print(register.items)  # List of items
print(register.void_last_transaction())  # Void the last transaction
print(register.total)  # Total after voiding
print(register.items)  # Updated list of items
