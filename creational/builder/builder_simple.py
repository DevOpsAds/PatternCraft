from creational.interfaces.person_inter  import Person

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def new_person(self):
        self.person = Person()

    def set_name(self, name):
        self.person.name = name

    def set_age(self, age):
        self.person.age = age

    def get_result(self):
        return self.person

