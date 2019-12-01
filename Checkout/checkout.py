class Checkout:
    class Discount:
        def __init__(self, num_of_items, price):
            self.num_of_items = num_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_discount(self, item, number_of_items, price):
        discount = self.Discount(number_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception('Bad Item')
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, num_of_items in self.items.items():
            total += self.calculate_item_total(item, num_of_items)
        return total

    def calculate_item_total(self, item, num_of_items):
        item_total = 0
        if item in self.discounts:
            item_total += self.calculate_item_discounted_total(
                item,
                num_of_items
            )
        else:
            item_total += self.prices[item] * num_of_items
        return item_total

    def calculate_item_discounted_total(self, item, num_of_items):
        discount = self.discounts[item]
        item_total_with_discount = 0
        item_total_with_discount += discount.price * (
            num_of_items // discount.num_of_items
        )
        item_total_with_discount += self.prices[item] * (
            num_of_items % discount.num_of_items
        )
        return item_total_with_discount
