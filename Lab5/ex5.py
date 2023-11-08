class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

    def sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, is_domesticated):
        super().__init__(name)
        self.is_domesticated = is_domesticated

    def move(self):
        return f"{self.name} walks or runs."

    def sound(self):
        return f"{self.name} makes a sound(depends)."

    def is_domesticated(self):
        return f"{self.name} is domesticated: {self.is_domesticated}"


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def move(self):
        if self.can_fly:
            return f"{self.name} flies."
        else:
            return f"{self.name} walks."

    def sound(self):
        return f"{self.name} chirps."


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)


    def move(self):
        return f"{self.name} swims."

    def sound(self):
        return f"{self.name} does not make a sound."


mammal = Mammal('Dog', True)
print(mammal.move())
print(mammal.sound())

bird = Bird('Eagle', True)
print(bird.move())
print(bird.sound())

fish = Fish('Shark')
print(fish.move())
print(fish.sound())
