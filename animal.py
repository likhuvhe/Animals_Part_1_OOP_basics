class Animal:
    def __init__(self, name, eat):
        self.name = name

    def eat(self):
        print(f"{self.name} eat")        

class Cat(Animal):
    def sounds(self):
        print("Cat meows")

class Dog(Animal):
    def sounds(self):
        print("Dog bark")

PET_ADOPTED = []
class Home:
    def adopt_pet(self, animal):
        if  animal in PET_ADOPTED:
            raise TypeError("not ok at all")
        else:
            print("totally ok")

        PET_ADOPTED.append(animal)

    def make_all_sounds(self):
        for pet in PET_ADOPTED:
            pet.sounds()        
# dog = Dog("J", "jj")
# cat = Cat("k", "kk")
# home = Home()
# home.adopt_pet(dog)
# home.adopt_pet(cat)
# home.make_all_sounds()
# home.adopt_pet(dog)