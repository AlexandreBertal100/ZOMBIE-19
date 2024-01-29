class VaccinationMonade:
    def __init__(self, people):
        self.people = people

    def bind(self, func):
        return VaccinationMonade(func(**{"people":self.people}))