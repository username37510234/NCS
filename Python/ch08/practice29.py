class House:
    def __init__(self, location, house_type, deal_type,price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
    
houses = []
house2 = House("송파","빌라","월세","500","2000년")

houses.append(House("강남","아파트","매매","10억","2010년"))
houses.append(House("마포","오피스텔","전세","5억","2007년"))
houses.append(house2)

for house in houses:
    house.show_detail()