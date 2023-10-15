from Animal import *

class Bird(Animal):
    #override method
    def make_noise(self):
        print("Jib Jib")

nok = Bird()
nok.make_noise()