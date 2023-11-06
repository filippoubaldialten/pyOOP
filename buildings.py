class Buildings:
    # variabili di classe, sono variabili con valore comune per tutte le istanze
    working_hrs_per_day = 24
    n_buildings_in_village = 0

    # metodo costruttore, serve a fare le istanze a partire dall classe:
    def __init__(self, name, level, n_workers):
        # variabili di istanza, sono attributi propri di ogni istanza:
        self.x_name = name
        self.x_level = level
        self.x_n_workers = n_workers

    def format_banally_input_values(self):
        sheet = f"""
        ************************************************
        Building sheet.\n
        Name: {self.x_name}\n
        Level: {self.x_level}\n
        Workers:{self.x_n_workers}\n
        ************************************************"""

        return sheet

#qui viene richiamato il costruttore:
workshop = Buildings("workshop", 9, 5)

#qui richiamo il metodo per l'istanza e lo stampo
print(workshop.format_banally_input_values())

#provo in due passaggi, prima richiamo il metodo e poi stampo
workshop_info = workshop.format_banally_input_values()
print(workshop_info)

