from app.model.people import People
from app.model.people_state import People_State
from app.model import ZombieUltime, ZombieA, ZombieB, ZombieC, Zombie19, Zombie32
from app.model.vaccins.interface import IVaccin

class VaccinUltime(IVaccin):

    NAME = "Vaccin-Ultime"
    IMUNNISE = [ZombieUltime, ZombieA, ZombieB, ZombieC, Zombie19, Zombie32]

    def vaccination(self,**kwargs):

        p: People = kwargs.get("people",None)
        
        if p is not None:
            if isinstance(p.get_type_virus(), ZombieUltime) :
                p.__setattr__("immunity",self.IMUNNISE)
                p.set_state(People_State.HEALTHY)
                p.set_type_of_virus(None)
                p._infected_by = None
       



