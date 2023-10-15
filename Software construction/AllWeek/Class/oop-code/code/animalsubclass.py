from animal import *

# Lion Is-A Animal
# Cat Is-A Animal
# Wolf Is-A Animal
# Dog Is-A Animal

class Lion(Feline):
    # override method
    def make_noise(self):
        print('Roaring: Rrrrr!')

class Cat(Feline):
    def make_noise(self):
        print('Miaowing: Miaooo!')

class Wolf(Canine):
    def make_noise(self):
        print("Howling: ouoooo!")

class Dog(Canine):
    def make_noise(self):
        print('Barking: Woof Woof!')

