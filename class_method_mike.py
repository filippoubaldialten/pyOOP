from buildings import Buildings
from stable import Stable

hiding_place_string = "hiding_pl-10-5"
stable_string = "Stalla Traballa Balaccalla-20-111"

hiding_place_1 = Buildings.from_string_alternative_constructor(hiding_place_string)

print(hiding_place_1.format_banally_input_values())

stable_cl_mth = Stable.from_string_alternative_constructor(stable_string, [["ww", True], ["ss", False], ["xx", True]])

print(stable_cl_mth.format_banally_input_values())

print(hiding_place_1.sticudszy())
print(stable_cl_mth.sticudszy())
