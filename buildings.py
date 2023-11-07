def print_n_buildings():
    to_print = f"""
    ***************************************
    Numero di edifici nel villaggio: {Buildings.n_buildings_in_village}\n
    ***************************************
    """
    print(to_print)


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
        # tutte le volte che instanzio un edificio incremento il numero di edifici nel villaggio
        Buildings.n_buildings_in_village += 1

    def format_banally_input_values(self):
        sheet = f"""
        ************************************************
        Building sheet.\n
        Name: {self.x_name}\n
        Level: {self.x_level}\n
        Workers: {self.x_n_workers}\n
        Working hrs per day: {self.working_hrs_per_day}\n
        ************************************************"""

        return sheet

    def add_level(self):
        self.x_level += 1

    def subtract_level(self):
        self.x_level -= 1
