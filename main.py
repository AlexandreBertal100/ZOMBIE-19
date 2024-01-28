from app.service import PeopleService
from app.model.virus import Zombie19, Zombie32, ZombieB, ZombieC, ZombieUltime
from app.model.vaccins import VaccinA1,VaccinB1, VaccinUltime
if __name__ == '__main__':

    peopls = [

        {"name":"louise","age":5, "friend":["mélissa"]},
        {"name":"mélissa","age":32, "friend":["alex"]},
        {"name":"alex","age":10, "friend":["louis","jonathan"]},
        {"name":"louis","age":20,"friend":["yanis"]},
        {"name":"jonathan","age":33,"friend":["laurine"]},
        {"name":"yanis","age":40},
        {"name":"laurine","age":50}
    ]

    z19 = Zombie19()
    zb = ZombieB()
    z32 = Zombie32()
    zc = ZombieC()
    zu = ZombieUltime()

    vacA= VaccinA1()
    vacB= VaccinB1()
    vacUltime= VaccinUltime()


    ps= PeopleService()
    ps.create_people(peopls)
    
    print('\n======= Creation =========')
    ps.display_tree('louise')
    print('============================\n')

    ps.create_infected([{"name":"alex","virus":zu}])

    print('\n======= After Infection =========')
    ps.display_tree('louise')
    print('===================================\n')

    for people in ps.get_peoples():
        vacUltime.vaccination(**{"people" : ps.get_peoples()[people]})

    print('\n======= After Vaccination =========')
    ps.display_tree('louise')
    print('===================================\n')