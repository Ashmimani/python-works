class Dishes:
    def __init__(self,name,price,qty):

        self.name=name
        self.price=price
        self.qty=qty

    def __str__(self):
        return(self.name)


rice_instance=Dishes("rice",120,"half")

biriyani_instance=Dishes("biriyani",100,"Half")

class Resturant:

    def __init__(self,name,place):

        self.name=name
        self.place=place
        self.dishes=[]

    def add_dishes(self,dishes):
        self.dishes.append(dishes)

    def list_dishes(self):
        for i in self.dishes:
            print(i)

resturant_instance=Resturant("name","place")

resturant_instance.add_dishes(rice_instance)
resturant_instance.add_dishes(biriyani_instance)
resturant_instance.list_dishes()