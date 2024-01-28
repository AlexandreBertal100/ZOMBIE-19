from app.model.people_state import People_State

class People():

    NAME : str
    AGE : int
    
    def __init__(self,**kwargs):
        """
            age : age of this people
            name : name of this people
        """
        self.AGE = kwargs.get('age')
        self.NAME = kwargs.get('name')
        self._state = kwargs.get('state', People_State.HEALTHY) 
        self._social_group = kwargs.get('friend',[])
        self._type_of_virus = kwargs.get('type_of_virus', None)
        self._infected_by = None
        self.immunity = []
        self.vaccines = []
    
    def get_age(self):
        return self.AGE
    
    def get_name(self):
        return self.NAME
    
    def get_state(self):
        return self._state.value
    
    def get_social_group(self):
        return self._social_group
    
    def get_type_virus(self):
        return self._type_of_virus
    
    def set_state(self,new_state:People_State):
        self._state = new_state

    def set_type_of_virus(self,new_state):
        self._type_of_virus = new_state

    def set_social_group(self,new_social_group):
        self._social_group = new_social_group
    
    def is_infected(self):
        if self.get_state() == 2:
            return True
        else:
            return False

    def infection_in_process(self,virus,infected_name):
        print(f' {self.get_name()} has infected by {infected_name} with {virus.get_name()}')
        if self._state is not People_State.DEATH and virus not in self.immunity:
            self.set_state(People_State.INFECTED)
            self.set_type_of_virus(virus)
            self.progation_in_process()
            self._infected_by = infected_name
        else :
            print(f'{self.get_name()} can\'t be infected by {virus.get_name()}')

    def progation_in_process(self):
        print(f' {self.get_name()} spreads {self.get_type_virus().get_name()} to social group')
        if self.is_infected():
            self.get_type_virus().propagation(**{"peoples_to_infecte":self.get_social_group(), "infected_name":self.get_name()})


