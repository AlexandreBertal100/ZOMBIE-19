from app.service import PeopleService
from app.model.virus.zombie19 import Zombie19

class ZombieB(Zombie19):

    NAME = "Zombien19-B"

    def propagation(self,**kwargs):
        friends = PeopleService().find_friend_to_name(**{"name" : kwargs.get("infected_name")})
        if friends and len(friends) > 0:
            for people in friends:
              
                p =  PeopleService().get_people_by_name(people)
                if p.is_infected() == False:
                    p.infection_in_process(self,kwargs.get("infected_name"))

    
    def get_name(self):
        return self.NAME

