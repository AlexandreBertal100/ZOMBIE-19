from app.model.people import People

class PeopleService ():

    peoples_dict = {}

    def __init__(self):
        self.cache_get_people_by_name = {}
        self.cache_find_friend_to_name = {}

    def memoize_get_people_by_name(self, name):
        if name not in self.cache_get_people_by_name:
            self.cache_get_people_by_name[name] = self.peoples_dict[name]
        return self.cache_get_people_by_name[name]

    def memoize_find_friend_to_name(self, **kwargs):
        key = frozenset(kwargs.items())
        if key not in self.cache_find_friend_to_name:
            friends = [friend_name for friend_name, person in self.peoples_dict.items() if kwargs.get('name') in person.get_social_group()]
            self.cache_find_friend_to_name[key] = friends
        return self.cache_find_friend_to_name[key]
    
    def get_people_by_name(self, name: str):
        return self.memoize_get_people_by_name(name)
    
    def find_friend_to_name(self, **kwargs):
        return self.memoize_find_friend_to_name(**kwargs) 

        return self.peoples_dict
    
    def get_all_peoples(self):
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
 
        
