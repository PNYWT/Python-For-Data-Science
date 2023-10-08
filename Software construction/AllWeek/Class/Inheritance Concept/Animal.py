class Animal:

    def __init__(self, name) -> None:
        self.name = name

    def eat(self, food):
        print(self.name, "is eating", food)

class Dog(Animal):
    pass

animal = Animal("Coin")
dog = Dog("Penny")
print(dog.name)
dog.eat("airpod")

print(isinstance(animal, Dog))
print(isinstance(animal, Animal))
print(issubclass(Dog, Animal))