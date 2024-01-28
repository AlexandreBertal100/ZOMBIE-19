from app.model.virus.zombie19 import Zombie19
from app.service.people_service import PeopleService

class ZombieC(Zombie19):

    NAME = "Zombie-C"

    def propagation(self, **kwargs):
        ascend = PeopleService().find_friend_to_name(**{"name": kwargs.get("infected_name")})
        descend = kwargs.get("peoples_to_infecte")

        for i, people in enumerate(ascend + descend):
            # Infecter une personne sur deux, alternant entre l'ascendant et le descendant
            if i % 2 == 0:
                p = PeopleService().get_people_by_name(people)
                if p.is_infected() == False:
                    p.infection_in_process(self, kwargs.get("infected_name"))
                    
    def get_name(self):
        return self.NAME