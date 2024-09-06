class Mobile:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display_mobile(self):
        print(self.name,self.price)

    def __str__(self):
        return self.name

mobile_instance=Mobile("samsung",15000)
mobile_instance.display_mobile()