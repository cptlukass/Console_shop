class Product:
    unique_id = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.unique_id
        Product.unique_id += 1


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        self.products[product.id] = product
        if product.id not in self.quantities:
            self.quantities[product.id] = 1
        else:
            self.quantities[product.id] += 1

    def remove_product(self, product):
        if product.id in self.products:
            del self.products[product.id]
            del self.quantities[product.id]
        pass

    def change_product_quantity(self, product, new_quantity):
        if product.id not in self.quantities:
            pass
        elif new_quantity == 0:
            del self.quantities[product.id]
        elif new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        else:
            self.quantities[product.id] = new_quantity

    def get_receipt(self):
        receipt = ""
        total_sum = 0
        for i in self.quantities:
            if self.quantities[i] < 3:
                receipt += f"{self.products[i].name} - ilość: {self.quantities[i]}, " \
                           f"cena: {self.products[i].price}zł, " \
                           f"suma: {self.products[i].price * self.quantities[i]}zł\n"
                total_sum += (self.products[i].price * self.quantities[i])
            else:
                receipt += f"{self.products[i].name} - ilość: {self.quantities[i]}, " \
                           f"cena: {self.products[i].price}zł, " \
                           f"suma: {round((self.products[i].price * self.quantities[i]) * 0.7, 2)}zł\n"
                total_sum += (self.products[i].price * self.quantities[i]) * 0.7
        receipt += f"\nSuma: {round(total_sum, 2)}zł"
        return receipt


bread = Product('Chleb', 2.70)
ham = Product('Szynka', 8.40)
cheese = Product('Ser', 4.40)
chive = Product('Szczypiorek', 1.50)
pepper = Product('Papryka', 2.35)

print(bread.id)
print(pepper.id)
print(pepper.name)
print(pepper.price)

cart = ShoppingCart()

print(cart.products)
print(cart.quantities)
print(cart.get_receipt())

cart.add_product(bread)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(pepper)
cart.add_product(chive)
cart.change_product_quantity(pepper, 3)
print(cart.products)
print(cart.quantities)

cart.remove_product(bread)
print(cart.get_receipt())
