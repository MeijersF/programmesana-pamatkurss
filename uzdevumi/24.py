"""
Šī prgoramma aprēkina spēlētāja atlikušos dzīvības punktus.
"""


speletajavards = "Anna"
hp_punkti = 100
uzbrukuma_jauda = 25

atlikums = hp_punkti - uzbrukuma_jauda
# Pirmās trīs rindas definē, kas ir kas - tās ir vajadzīgas, lai dators saprastu, kas jādara. 5. rinda nosaka, kā aprēķināt attiecīgo vērtību. 6. rinda vajadzīga, lai iegūtu punktu par uzdevuma izpildi.
print(f"{speletajavards}, tev ir atlikuši {atlikums} dzīvības punkti.")
