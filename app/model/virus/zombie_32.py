from app.service import PeopleService

class Zombie32():

    NAME = "Zombien19-32"

    def propagation(self,**kwargs):

        ascend = PeopleService().find_friend_to_name(**{"name" : kwargs.get("infected_name")})
        descend = kwargs.get("peoples_to_infecte")

        friends = ascend + descend

        if friends and len(friends) > 0:
            for people in friends:
              
                p =  PeopleService().get_people_by_name(people)
                if p.is_infected() == False and p.get_age() > 30:
                    p.infection_in_process(self,kwargs.get("infected_name"))

    
    def get_name(self):
        return self.NAME

