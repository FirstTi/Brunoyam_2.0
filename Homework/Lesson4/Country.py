# Написать программу с пустым классом Country. Описать наследуемые классы стран.
# Добавить каждому классу поле population
# Описать метод setPopulation (задать объекту св-во population)
# Описать метод getPopulation (получить из объекта св-во population)

class Country:
    def __init__(self, population):
        self.population = population
        #self.name = name ????
    
    def getPopulation(self):
        
        #return self.name, self.population
        return self.population

class Bulgaria(Country):
    population = 75
    pass


class Canada(Country):
    population = 100
    #self.name = name????
    pass

class Germany(Country):
    population = 120
    pass

print(Canada.population)
print(Germany.population)

