def voitis_nurkademangu(t):
    if t[0][0] == "X" and t[0][4] == "X" and t[4][0] == "X" and t[4][4] == "X":
        return True
    else:
        return False

def x_peadiagonaalil(t):
    x_arv = 0
    for i in range(5):
        if t[i][i] == "X":
            x_arv = x_arv + 1
    return x_arv

def x_korvaldiagonaalil(t):
    x_arv = 0
    for i in range(5):
        if t[i][4-i] == "X":
            x_arv = x_arv + 1
    return x_arv

def voitis_diagonaalidemangu(t):
    if x_korvaldiagonaalil(t) == 5 and x_peadiagonaalil(t) == 5:
        return True
    else:
        return False

def voitis_taismangu(t):
    for i in t:
        for v in i:
            if v != "X":
                return False

    return True