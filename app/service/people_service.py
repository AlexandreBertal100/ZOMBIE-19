from app.model.people import People

class PeopleService ():

    peoples_dict = {}
            
    def get_social_by_name(self,name:str):
        return self.get_people_by_name(name).get_social_group()
        
    def get_people_by_name(self,name:str):
        return self.peoples_dict[name]
        
    def get_peoples(self):
        return self.peoples_dict
    
    def create_people(self,peoples_to_create):
        
        for people in peoples_to_create:
            self.peoples_dict[people.get("name")] = People(**people)
    
    def create_infected(self,firts_infected):
        for infected in firts_infected:
            people_to_infect = self.get_people_by_name(infected['name'])
            people_to_infect.infection_in_process(infected['virus'],"X")
    
    def display_tree(self,node, depth=0):

        node = self.get_people_by_name(node)

        indent = "  " * depth
        status = node._state.name
        virus = node.get_type_virus().get_name() if node.get_type_virus() is not None else "Nothing"
        print(f"{indent}- {node.get_name()} (Age: {node.get_age()}, Status: {status}, Virus: {virus})")
        for child in node.get_social_group():
            self.display_tree(child, depth + 1)

    def find_friend_to_name(self,**kwargs):
        friends = []
        for name, persone in self.peoples_dict.items():
            if kwargs.get('name') in persone.get_social_group():
                friends.append(name)

        return friends
    
                
    
    
        
