from app.service import PeopleService

class Zombie19():

    NAME = "Zombie19"

    def propagation(self,peoples_to_infecte,infected_name):
        if peoples_to_infecte and len(peoples_to_infecte) > 0:
            for people in peoples_to_infecte:
                
                p =  PeopleService().get_people_by_name(people)
                if p.is_infected() == False:
                    p.infection_in_process(self,infected_name)
    
    def get_name(self):
        return self.NAME

