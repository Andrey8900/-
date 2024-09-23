class Animal:
    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date

    def get_name(self):
        return self._name

    def get_birth_date(self):
        return self._birth_date

class Pet(Animal):
    pass

class PackAnimal(Animal):
    pass
