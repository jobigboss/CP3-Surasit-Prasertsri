class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastName,"'s cart")
        print("Added product to", self.name, self.lastName, "'s cart")

customer1 = Customer()
customer1.name = "Surasit"
customer1.lastName = "Surasit  Prasertsri"
customer1.age = 27

customer2 = Customer()
customer2.name = "Manom"
customer2.lastName = "Manom  Suwandee"
customer2.age = 20

customer3 = Customer()
customer3.name = "Jaiaree"
customer3.lastName = "Jaiaree  Prasertsri"
customer3.age = 12

customer4 = Customer()
customer4.name = "Bigboss"
customer4.lastName = "Bigboss  Srisompod"
customer4.age = 15
customer1.addCart()