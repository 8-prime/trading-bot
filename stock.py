
class Stock:

    name = ""
    price_time_of_purchase = 0
    sliding_average = 0
    amount_held = 0
    current_price = 0

    def __init__(self, price_time_of_purchase = 0, sliding_average = 0, amount_held = 0, current_price = 0, name = "")

    def get_price():
        return self.current_price

    def set_price(new_price):
        self.current_price = new_price
    
    def get_sliding_average():
        return sliding_average
    
    def set_sliding_average(new_average):
        self.sliding_average = new_average

    def get_amount_held():
        return self.amount_held
    
    def set_amount_held(new_amount):
        self.amount_held = new_amount

    def get_name():
        return self.name