# Practice Question
''' create a class called order which stores items and its price
use dunder function __gt__() to convey that
order 1> order 2
if
price of order1 is greater than order 2'''


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, Order2):
        return self.price > Order2.price

Order1 = Order('Chips',102)
Order2 = Order('Biscuit', 101)
print(Order1>Order2)