fail = open("toad.txt", encoding="UTF-8")

tubade_tabel = []

for rida in fail: # iga rea jaoks failist
    korruse_toad = [] # kogume ühe korruse tubasid
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korruse_toad.append(int(osa)) # järjekordne tuba juurde

    tubade_tabel.append(korruse_toad) # korruse tubade järjend juurde

fail.close()

for korrus, toad in enumerate(tubade_tabel):
    if (korrus % 2) != 0:
        for tuba in toad:
            if (tuba % 2) == 0:
                print(tuba)