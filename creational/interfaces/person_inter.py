class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
