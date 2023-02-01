class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = [
            {"name": "Beer", "price": 3.50, "alcohol_level": 2, "stock": 100,},
            {"name": "Wine", "price": 4.80, "alcohol_level": 3, "stock": 150,},
            {"name": "Whisky", "price": 6.00, "alcohol_level": 4, "stock": 50,},
            ]

    def sell_drink(self, customer, drink):
        for item in self.drinks:
            if item["stock"] == 0 or self.is_customer_underage(customer) or self.is_customer_drunk(customer):
                break
            elif item["name"] == drink.name:
                customer.buy_drink(drink)
                self.till += drink.price
                item["stock"] -= 1
    
    def is_customer_underage(self, customer):
        if customer.age < 18:
            return True

    def is_customer_drunk(self, customer):
        if customer.drunkeness >= 10:
            return True

    def stock_check(self):
        names = []
        stock = []
        values = []
        for item in self.drinks:
            names.append(item["name"])
            stock.append(item["stock"])
            values.append(item["price"])
        total = 0
        index = 0 
        for i in stock:
            total += stock[index] * values[index]
            index += 1
            
        return f"There are {stock[0]} servings of {names[0].lower()}, {stock[1]} servings of {names[1].lower()} and {stock[2]} servings of {names[2].lower()}. The total stock value is {total}"