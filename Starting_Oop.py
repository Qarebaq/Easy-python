class Animal:
    zoo_name = "Eram Zoo"  

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Sound: {self.sound}, Zoo: {Animal.zoo_name}")

    def __str__(self):
        return f"Animal ---> name={self.name}, species={self.species}, age={self.age}, sound={self.sound}, zoo_name={Animal.zoo_name}"


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        Animal.__init__(self, name, species, age, sound)  # استفاده بدون super
        self.wing_span = wing_span

    # بازنویسی متد make_sound
    def make_sound(self):
        print(f"{self.name} Makes a Sound: {self.sound}")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Sound: {self.sound}, Wing Span: {self.wing_span}, Zoo: {Animal.zoo_name}")


lion = Animal("Leo", "Lion", 5, "Roar")
print(lion)                
lion.make_sound()          
lion.info()              

print()

Morgh = Bird("Chikchik", "Morgh", 2, "goood gooda!", 0.3)
print(Morgh)             
Morgh.make_sound()
Morgh.info()        
