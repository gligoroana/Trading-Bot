# constante
pret_1 = [7000, 6950, 6900, 6850, 6900, 7000,
        7200, 6800, 6750, 6700, 6650, 6700,
        6600, 6500, 6450, 6500, 6550, 6600,
        6550, 6500, 6450, 6400, 6350, 6400, 6450,
        6350, 6400, 6300, 6250, 6200, 6250,
        6300, 6350, 6300, 6250, 6200, 6150, 6100, 6000]

pret = [6999, 6980, 6975, 6970, 6975, 6980,
        6985, 6990, 7000, 7010, 7020,
        7005, 6950, 6945, 6940, 6930,
        6935, 6940, 6950, 6960, 6970,
        6960, 6950, 6940, 6945, 6950,
        6955, 6960, 6975, 6980]

portofoliu = []
max_portofoliu = 5
portofelul_meu = 3700
tranzactii = 0
cantitate_cumparata = 0.1


class Tranzactie:
    def __init__(self, pret, vinde_ma_castig, vinde_ma_pierd):
        self.pret = pret
        self.vinde_ma_castig = vinde_ma_castig
        self.vinde_ma_pierd = vinde_ma_pierd


# simulare tranzactii
for zi in range(len(pret)):
    print("ziua: ", zi, ", pretul: ", pret[zi], ", marime portofoliu: ", len(portofoliu), "portofelul_meu: ", portofelul_meu)
    if len(portofoliu) < max_portofoliu:
        if pret[zi] < pret[0] - 20:
            print("cumpar cu ", pret[zi])
            new_tranzactie = Tranzactie(pret[zi], pret[zi] + 40, pret[zi] - 60)
            portofoliu.append(new_tranzactie)
            portofelul_meu = portofelul_meu - pret[zi]*cantitate_cumparata - 0.0025*pret[zi]*cantitate_cumparata
            tranzactii = tranzactii + 1
        else:
            print("nu cumpar - destul de scump")
    else:
        print("nu cumpar - portofoliu max")

    if zi >= 1:
        de_sters = []
        for j in range(len(portofoliu)):
            if pret[zi] > portofoliu[j].vinde_ma_castig:
                print("vand castig - il vand pe", portofoliu[j].pret)
                tranzactii = tranzactii + 1
                de_sters.append(portofoliu[j])
                portofelul_meu = portofelul_meu + pret[zi]*cantitate_cumparata - 0.0025*pret[zi]*cantitate_cumparata
                print("portofelul_meu: ", portofelul_meu)
            if pret[zi] < portofoliu[j].vinde_ma_pierd:
                print("vand pierd - il vand pe", portofoliu[j].pret)
                tranzactii = tranzactii + 1
                de_sters.append(portofoliu[j])
                portofelul_meu = portofelul_meu + pret[zi]*cantitate_cumparata - 0.0025*pret[zi]*cantitate_cumparata
                print("portofelul_meu: ", portofelul_meu)
        for k in range(len(de_sters)):
            #print(portofoliu)
            portofoliu.remove(de_sters[k])
            #print(portofoliu)

print("-----------------------")
print("portofelul meu: ", portofelul_meu)
for i in range(len(portofoliu)):
    portofelul_meu = portofelul_meu + pret[-1]*cantitate_cumparata - 0.0025*pret[-1]*cantitate_cumparata

print("portofelul_meu: ", portofelul_meu)
print("tranzactii: ", tranzactii)