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

    def __init__(self,weight,growth_rate):
        self.weight = weight
        self.days_growing = 0
        self.growth_rate = growth_rate
        #slef.food_need = 

    def get_weight(self):
        print(self.weight)

list = []
for i in range(5):
    list.append(Animal(i,i*2))

for i in range(5):
    list[i].get_weight()
print(list)
