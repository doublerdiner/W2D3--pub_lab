class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name 
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.increase_drunkeness(drink)
    
    def increase_drunkeness(self, drink):
        self.drunkeness += drink.alcohol_level

    def buy_food(self, food):
        self.wallet -= food.price
        self.drunkeness -= food.rejuvination_level