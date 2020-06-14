class Hero:
    #class variable
    calculation = 0

    def __init__(self, name, health, power, armor):
        #Instance Variables
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        Hero.calculation += 1
        print("Creating a hero called " + name)


hero1 = Hero("Dio Brando", 200, 100, 30)
print(Hero.calculation)
hero2 = Hero("Jotaro Kujou", 180, 130, 25)
print(Hero.calculation)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(Hero.__dict__)
