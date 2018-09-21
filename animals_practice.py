def in_int(message):
    valid = False
    while valid == False:
        init = input(message)
        try:
            number = int(init)
            valid = True
        except:
            print('That is not a valid number')
    return number

class Animal():

    def __init__(self, weight, growth_rate, food_need, water_need, status, name):
        self.weight = weight
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        c = water_need
        self.status = status
        self.type = 'generic'
        self.name = name

    def needs(self):
        print('Food need:  '+self.food_need)
        print('Water need: '+self.water_need)

    def report(self):
        print('Weight:       '+self.wieght)
        print('Days growing: '+self.days_growing)
        print('Growh rate:   '+self.growth_rate)
        print('Food need:    '+self.food_need)
        print('Water need:   '+self.water_need)
        print('Status:       '+self.status)
        print('Type:         '+self.type)
        print('Name:         '+self.name)

    def update_status(self, status):
        self.status = status

    def grow(self, food, water):
        if self.food_need < food and self.growth_rate < water:
            self.weight += self.growth_rate
        else:
            print('Not enough resources for growth.')

class Cow(Animal):

    def __init__(self, weight, growth_rate, food_need, water_need, status, name):
        self.weight = weight
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.food_need = food_need
        c = water_need
        self.status = status
        self.type = 'generic'
        self.name = name
    
    def grow(self, food, water):
        if self.food_need < food and self.growth_rate < water:
            self.weight += self.growth_rate*0.93
        else:
            print('Not enough resources for growth.')
