from app.model.people import People
from app.model.people_state import People_State
from app.model import ZombieA,ZombieB,ZombieC,Zombie32,ZombieUltime
from app.model.vaccins.interface import IVaccin

class VaccinA1(IVaccin):

    NAME = "Vaccin-A.1"
    IMUNNISE = [ZombieA,ZombieB,ZombieC,Zombie32,ZombieUltime] 

    def vaccination(self,**kwargs):

        p: People = kwargs.get("people",None)
        
        if p is not None:
            
            if p.get_age() < 31:
                p.__setattr__("immunity",self.IMUNNISE)
                
                if isinstance( p.get_type_virus(), ZombieA) or isinstance( p.get_type_virus(), Zombie32):
                    p.set_state(People_State.HEALTHY)
                    p.set_type_of_virus(None)
                    p._infected_by = None



