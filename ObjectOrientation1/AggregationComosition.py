class FoodItem:
    def __init__(self,name,price,rating,is_veg):
        self.name = name
        self.price = price
        self.rating = rating
        self.is_veg = is_veg
class DelivaryAgent:
    def __init__(self,name,rating,phone):
        self.name = name
        self.rating = rating
        self.phone = phone
class Resaurant:
    def __init__(self,name,address,rating):
        self.name = name
        self.address = address
        self.rating = rating 
        # composition --> create object has in instance variable 
        self.pizza = FoodItem('pizza',500,4.5,True) 
    # Aggegation --> creating method
    def assign_delivery_agent(self,agent):
        self.agent = agent
def main():
    r = Resaurant('XYZ','Bang',5)
    d = DelivaryAgent('rohit',4.5,7676115988)
    r.assign_delivery_agent(d)
    print(r.pizza.price) # reach price of pizza via Restaurant using r 
    print(r.agent.name) # reach via Restaurant object
    # print(pizza.price) # not directly accesable --> composition --> strong bond with Restaurant object.
    print(d.name) # directly accessable because --> aggregation --> weak bond with Restaurant object.
    del r
if __name__ == '__main__':
    main()


# inner class --> class under class
class DelivaryAgent:
    def __init__(self,name,rating,phone):
        self.name = name
        self.rating = rating
        self.phone = phone
class Resaurant:
    class FoodItem:
        def __init__(self,name,price,rating,is_veg):
            self.name = name
            self.price = price
            self.rating = rating
            self.is_veg = is_veg
    def __init__(self,name,address,rating):
        self.name = name
        self.address = address
        self.rating = rating 
        # composition --> create object has in instance variable 
        self.pizza = Resaurant.FoodItem('pizza',500,4.5,True) 
    # Aggegation --> creating method
    def assign_delivery_agent(self,agent):
        self.agent = agent
def main():
    r = Resaurant('XYZ','Bang',5)
    d = DelivaryAgent('rohit',4.5,7676115988)
    r.assign_delivery_agent(d)
    print(r.pizza.price) # reach price of pizza via Restaurant using r 
    print(r.agent.name) # reach via Restaurant object
    # print(pizza.price) # not directly accesable --> composition --> strong bond with Restaurant object.
    print(d.name) # directly accessable because --> aggregation --> weak bond with Restaurant object.
    del r
if __name__ == '__main__':
    main()