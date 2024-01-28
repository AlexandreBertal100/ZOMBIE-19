from app.model.people import People
from app.model.people_state import People_State
from app.model import ZombieB,ZombieC

class VaccinB1():

    NAME = "Vaccin-B.1"
    IMUNNISE = []
    make_a_death = False 

    def vaccination(self,**kwargs):

        p: People = kwargs.get("people",None)
        
        if p is not None:
            
            if self.make_a_death is not True:
                if  isinstance( p.get_type_virus(), ZombieB) or isinstance( p.get_type_virus(), ZombieC) :
                    p.set_state(People_State.HEALTHY)
                    p.set_type_of_virus(None)
                    p._infected_by = None
                    self.make_a_death = True
            else:
                p.set_state(People_State.DEATH)
                self.make_a_death = False




