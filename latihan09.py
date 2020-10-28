personandpets = [
    {
        "name": "John Doe",
        "pets": [
            {"name": "Rooster"},
            {"name": "Dog"}
        ]
    },
    {
        "name": "Luke Skywalker",
        "pets": [
            {"name": "Duck"},
            {"name": "Camel"}
        ]
    },
    {
        "name": "Padme Amidala",
        "pets": [
                {"name": "Bird"},
                {"name": "Fish"}
        ]
    }
]


class Person:  # template
    pass


person1 = Person()  # object/instance
person2 = Person()
person3 = Person()

person1.name = "John Doe"
person1.pet = "Rooster, Dog"
person2.name = "Luke Skywalker"
person2.pet = "Duck", "Camel"
person3.name = "Padme Amidala"
person3.pet = "Bird", "Fish"

print(person1.__dict__, person2.__dict__, person3.__dict__)


# first class
class PersonPets:
    def __init__(self, person=None, pet=None):
        self.person = person
        self.pet = pet

    def getPetbyPerson(self):
        for x in personandpets:
            print(x)

    def getPetbyPerson(self):
        for x in personandpets:
            if x['name'] == self.person:
                for p in x['pets']:
                    print(p)


pp = PersonPets(person='Padme Amidala')
pp.getPetbyPerson()
