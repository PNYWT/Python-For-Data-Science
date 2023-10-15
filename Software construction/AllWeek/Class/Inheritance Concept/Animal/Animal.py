class Animal:

    def __init__(self, name = "") -> None:
        self.name = name

    def eat(self, food):
        print(self.name, "is eating", food)

    def sleep(self):
        print("Noises...")

    def roam(self):
        print("Roamin on the plain.")

class Lion(Animal):
    def make_noise(self):
        print("Roaring: Rrrrrrr!")

class Cat(Animal):
    def make_noise(self):
        print("Miaowing: Miaooo!")

class Wolf(Animal):
    def make_noise(self):
        print("Howling: Ouoooo!")

class Gog(Animal):
    def make_noise(self):
        print("Barking: Woof Woof!")

def main():
    print("\nWolf\n=====")
    wolfie = Wolf()
    wolfie.make_noise()
    wolfie.roam()
    wolfie.sleep()
       
main()


# animal = Animal("Coin")
# dog = Dog("Penny")
# print(dog.name)
# dog.eat("airpod")

# print(isinstance(animal, Dog))
# print(isinstance(animal, Animal))
# print(issubclass(Dog, Animal))