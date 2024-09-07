# Declaration and Initialization
lagos_state = ["Agege", "Bariga", "Oshodi", "Ketu", "Ikorodu"]

# Append new list
lagos_state.append("Ikoyi")

# Add new list to index 2
lagos_state.insert(2, "Iyana-Ipaja")

agbado = ["Kola", "Alakuko"]

# Add agbado to lagos state list
lagos_state.extend(agbado)

for index, items in enumerate(lagos_state, start=1):
    print(index, items)