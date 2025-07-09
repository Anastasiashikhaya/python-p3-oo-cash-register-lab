class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.last_transaction > 0:
            if self.total == 0:
                self.items = []

# Test code that runs when executed directly
if __name__ == "__main__":
    print("Testing CashRegister class...")
    register = CashRegister(20)
    register.add_item("Apple", 0.99)
    print(f"Total after adding Apple: ${register.total}")
    register.add_item("Banana", 1.50, 2)
    print(f"Total after adding Bananas: ${register.total}")
    print(f"Items in cart: {register.items}")
    register.apply_discount()
    print(f"Total after discount: ${register.total}")
    register.void_last_transaction()
    print(f"Total after voiding: ${register.total}")
    print("Tests completed!")