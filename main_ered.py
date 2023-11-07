# non si fa così ma come Smithy (stable esempio sbagliato)
#import stable
from buildings import Buildings
from smithy import Smithy
from stable import Stable


# Classi eredi
print("*********** Classi Eredi ****************************")
print("*****************************************************")
smithy_1 = Smithy("Smithy 1", 20, 111)
# stable_1 = stable.Stable("Stable 1", 20, 99) <- sbagliato
stable_1 = Stable("Stable 1", 20, 99)
print(smithy_1.format_banally_input_values())
print(Buildings.format_banally_input_values(smithy_1))
print(stable_1.format_banally_input_values())
print(Buildings.format_banally_input_values(stable_1))

# # HELP (Lo tengo commentato perché rompe...)
# print("*********** HELP ************************************")
# print("*****************************************************")
# print(help(Buildings))
# print(help(Smithy))
# # print(help(stable)) <- sbagliato
# print(help(stable_1))

# Stalla avanzata
print("*********** Stalla avanzata ****************************")
print("********************************************************")
stable_2 = Stable("Stalla 2", 19, 88, [["sc", False], ["lc", False], ["hc", True]])
print(stable_2.format_banally_input_values())

# ADD LEVEL
print("*********** ADD LEVEL **********************************")
print("********************************************************")
stable_level = Stable("Stalla costruzione", 17, 66, [["sc", False], ["lc", False], ["hc", True]])
print("********************Livello prima **********************")
print(stable_level.format_banally_input_values())
# Il metodo è nella classe padre quindi si chiama così:
Buildings.add_level(stable_level)
print("********************Livello dopo ***********************")
print(stable_level.format_banally_input_values())

# ADD LEVEL senza usare variabili classe figlia
print("*********** ADD LEVEL **********************************")
print("********************************************************")
stable_x = Stable("Stalla x", 17, 66, )
print("********************Livello prima **********************")
print(stable_x.format_banally_input_values())
# Il metodo è nella classe padre quindi si chiama così:
Buildings.add_level(stable_x)
print("********************Livello dopo ***********************")
print(stable_x.format_banally_input_values())
