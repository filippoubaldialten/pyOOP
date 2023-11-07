import buildings


class Smithy(buildings.Buildings):
    troops = False

    # Versione personalizzata init
    def __init__(self, name, level, n_workers, research=None, active=None):
        # variabili gestite dalla classe padre (se le va a prendere lì)
        super().__init__(name, level, n_workers)
        # variabili specifiche della classe figlia (in questo caso due liste)
        if research is None:
            research = []
        else:
            self.x_research = research
        if active is None:
            active = []
        else:
            self.x_active = active
