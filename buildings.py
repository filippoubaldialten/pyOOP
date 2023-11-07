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
    # possono essere modificate da metodi di classe

    # metodo costruttore, serve a fare le istanze a partire dall classe:
    # il self è una referenza a ciascuna istanza creata a partire dalla classe
    def __init__(self, name, level, n_workers):
        # variabili di istanza, sono attributi propri di ogni istanza:
        self.x_name = name
        self.x_level = level
        self.x_n_workers = n_workers
        # tutte le volte che instanzio un edificio incremento il numero di edifici nel villaggio
        Buildings.n_buildings_in_village += 1

    # metodo di classe, alternativo a init (passa la classe "cls")
    @classmethod
    def from_string_alternative_constructor(cls, hp_string, *args):
        name, level, n_workers = hp_string.split("-")
        return cls(name, level, n_workers, *args)

    #  può anche essere usato inmodo diverso a seconda della sottoclasse da cui è richiamato
    @classmethod
    def sticudszy(cls):
        if cls.__name__ == "Stable":
            return ">>>>>>> Stable"
        else:
            return ">>>>>>> Not a Stable"

    @staticmethod
    def info_program():
        info = """
        scritto da: \n
        Filippo Ubaldi"""

        return info

    # metodo di istanza passa l'istanza tramite "self"
    # il self è una referenza a ciascuna istanza creata a partire dalla classe
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

    # il self è una referenza a ciascuna istanza creata a partire dalla classe
    def add_level(self):
        self.x_level += 1

    # il self è una referenza a ciascuna istanza creata a partire dalla classe
    def subtract_level(self):
        self.x_level -= 1
