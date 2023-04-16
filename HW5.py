# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания
#     значений этого атрибута нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий

class Animal:
    def __init__(self, name, species, sound):
        self._name = name  # атрибут с уровнем доступа private
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self._name} says '{self.sound}'")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat", "meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog", "woof")



my_cat = Cat("Dusa")
my_dog = Dog("Tirol")

print(my_cat.make_sound())
print(my_dog.make_sound())

print(my_cat.get_name())
my_cat.set_name("Chicha")
print(my_cat.get_name())
