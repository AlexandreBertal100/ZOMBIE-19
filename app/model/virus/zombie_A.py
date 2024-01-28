from app.service import PeopleService
from app.model.virus.zombie19 import Zombie19

class ZombieA(Zombie19):

    NAME = "Zombien19-A"

    def propagation(self,**kwargs):
        peoples_to_infecte = kwargs.get("peoples_to_infecte")
        
        if peoples_to_infecte and len() > 0:
            for people in peoples_to_infecte:
                p =  PeopleService().get_people_by_name(people)
                if p.is_infected() == False:
                    p.infection_in_process(self,kwargs.get("infected_name"))
    
    def get_name(self):
        return self.NAME

