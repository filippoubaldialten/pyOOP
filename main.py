import buildings
import smithy
import stable
from buildings import Buildings

#instanzio il workshop
# qui viene richiamato il costruttore:
workshop = Buildings("workshop", 9, 5)
# # qui richiamo il metodo per l'istanza e lo stampo (commentato ma funziona)
# print(workshop.format_banally_input_values())
# provo in due passaggi, prima richiamo il metodo e poi stampo
workshop_info = workshop.format_banally_input_values()
print(workshop_info)

#instanzio farm: building che si ferma di notte
farm = Buildings("farm", 15, 100)
# modifico le ore di lavoro giornaliere
farm.working_hrs_per_day -= 8
# verifico le ore di lavoro giornaliere stampandole
farm_info = farm.format_banally_input_values()
print(farm_info)

print("numero di edifici: " + str(Buildings.n_buildings_in_village))
print(Buildings.n_buildings_in_village)
buildings.print_n_buildings()
# timber = Buildings("timber camp", 17, 88)
# clay = Buildings("clay pit", 18, 94)
