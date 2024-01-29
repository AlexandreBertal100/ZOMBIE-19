from app.tools import VaccinationMonade


class VaccinationService():
    
    def vaccination_in_process(self,peoples, vaccins):
        if not peoples or not vaccins:
            return
        
        for person_name, person_data in peoples.items():
            for vaccin in vaccins:
                VaccinationMonade(person_data).bind(vaccin.vaccination)
