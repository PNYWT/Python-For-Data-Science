class Animal:
    def sleep(self):
        print('Sleeping: zzzz')

    def make_noise(self):
        print('Noises....')

    def roam(self):
        print('Roaming: ', endl='')

class Feline(Animal):
    def roam(self):
        super().roam()
        print("I'm roaming alone.")

class Canine(Animal):
    def roam(self):
        super().roam()
        print("I'm with my pack.")
