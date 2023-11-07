import buildings


class Stable(buildings.Buildings):
    troops = True

    def __init__(self, name, level, n_workers, recruitment=None):
        super().__init__(name, level, n_workers)
        if recruitment is None:
            self.x_recruitment = [[], [], []]
        else:
            self.x_recruitment = recruitment

    def format_banally_input_values(self):
        sheet = f"""
        [Tipo, Rec] :{self.x_recruitment}
        """
        return super().format_banally_input_values() + sheet
