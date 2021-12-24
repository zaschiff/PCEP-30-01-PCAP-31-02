# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animal:
    def __init__(self):
        print("Animal constructed....")

    def move(self):
        print("Animal moving...")

    def eat(self):
        print("Animal eating....")

class dog(Animal):
    def __init__(self, dog_name, dog_age):
        Animal.__init__(self)
        self.Name = dog_name
        self.Age = dog_age

    def move(self):
        print("Dog is walking...")
    
class bird(Animal):
    def __init__(self, bird_name, bird_age):
        Animal.__init__(self)
        self.Name = bird_name
        self.Age = bird_age

    def move(self):
        print("Bird is flying...")

class fish(Animal):
    def __init__(self, fish_name, fish_age):
        Animal.__init__(self)
        self.Name = fish_name
        self.Age = fish_age

    def move(self):
        print("Fish is swimming...")


toby = dog("toby", 3)
nemo = fish("nemo", 1)
tweety = bird("tweety", 2)

toby.move()
toby.eat()
nemo.move()
nemo.eat()
tweety.move()
tweety.eat()














































# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()