class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.cart = []

    def add_product(self, prd):
        self.cart.append(prd)
        print(f'{prd.name} added to the cart')
    
    def remove_product(self, name):
        for item in self.cart:
            if item.name.lower() == name.lower():
                self.cart.remove(item)
                print(f'{item.name} removed from the cart')
        return
    
    def total_price(self):
        total = 0
        if not self.cart:
            return None
        for item in self.cart:
            total += item.price
        return total

p1 = Product('Jeans', 999)
p2 = Product('Shampoo', 899)
p3 = Product('Shirt', 499)
p4 = Product('Fruits', 200)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
print(cart.total_price())
cart.add_product(p3)
cart.add_product(p4)
print(cart.total_price())
cart.remove_product('Jeans')
print(cart.total_price())