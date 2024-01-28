from app.model.virus.zombie19 import Zombie19
from app.service.people_service import PeopleService

class ZombieUltime(Zombie19):

    NAME = "Zombie-Ultime"

    def propagation(self, **kwargs):
        ascend = PeopleService().find_friend_to_name(**{"name": kwargs.get("infected_name")})

        if len(ascend) == 0:
            p = PeopleService().get_people_by_name(kwargs.get("infected_name"))
            if p.is_infected() == False:
                p.infection_in_process(self, kwargs.get("infected_name"))
        else:
            for i, people in enumerate(ascend):
                self.propagation(**{"infected_name":people})
            
