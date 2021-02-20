
class Stock:
    #name of the stock
    name = ""
    #in epoch time
    price_time_of_purchase = 0
    sliding_average = 0
    amount_held = 0
    current_price = 0
    price_hist = []

    def __init__(self, price_time_of_purchase = 0, sliding_average = 0, amount_held = 0, current_price = 0, name = "", price_hist = None):
        self.name = name
        self.price_time_of_purchase = price_time_of_purchase
        self.sliding_average = sliding_average
        self.amount_held = amount_held
        self.current_price = current_price
        self.price_hist = price_hist

    def get_price(self):
        return self.current_price

    def set_price(self, new_price):
        self.current_price = new_price
    
    def get_sliding_average(self):
        total = 0 
        usable_data = self.price_hist[0]['1. open']
        num_vals = len(usable_data)
        for i in range(len(usable_data)):
            total += usable_data[i]
        return total/num_vals
    
    def set_sliding_average(self, new_average):
        self.sliding_average = new_average

    def get_amount_held(self):
        return self.amount_held
    
    def set_amount_held(self, new_amount):
        self.amount_held = new_amount

    def get_name(self):
        return self.name

    def set_price_hist(self, new_hist):
        self.price_hist = new_hist
