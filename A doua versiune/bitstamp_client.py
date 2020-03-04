import time
import get_data
import CONSTANTS as CONST

MyData = get_data.Data(CONST.TICKER_LINK)


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

initial_price = MyData.get_last_price()


while True:

    price = MyData.get_last_price()
    print(price)


    # My Trade Strategy --- TO DO -> class Trader.

    print("pretul: ", price, ", marime portofoliu: ", len(portofoliu), ", portofelul_meu: ", portofelul_meu)
    if len(portofoliu) < max_portofoliu:
        if price < initial_price - 1:
            print("cumpar cu ", price)
            new_tranzactie = Tranzactie(price, price + 40, price - 60)
            portofoliu.append(new_tranzactie)
            portofelul_meu = portofelul_meu - price * cantitate_cumparata - 0.0025 * price * cantitate_cumparata
            tranzactii = tranzactii + 1
        else:
            print("nu cumpar - destul de scump")
    else:
        print("nu cumpar - portofoliu max")


    de_sters = []
    for j in range(len(portofoliu)):
        if price > portofoliu[j].vinde_ma_castig:
            print("vand castig - il vand pe", portofoliu[j].pret)
            tranzactii = tranzactii + 1
            de_sters.append(portofoliu[j])
            portofelul_meu = portofelul_meu + price * cantitate_cumparata - 0.0025 * price * cantitate_cumparata
            print("portofelul_meu: ", portofelul_meu)
        if price < portofoliu[j].vinde_ma_pierd:
            print("vand pierd - il vand pe", portofoliu[j].pret)
            tranzactii = tranzactii + 1
            de_sters.append(portofoliu[j])
            portofelul_meu = portofelul_meu + price * cantitate_cumparata - 0.0025 * price * cantitate_cumparata
            print("portofelul_meu: ", portofelul_meu)
    for k in range(len(de_sters)):
        # print(portofoliu)
        portofoliu.remove(de_sters[k])
        # print(portofoliu)

    print("-----------------------")
    print(portofelul_meu)
    for i in range(len(portofoliu)):
        print(portofoliu[i].pret)

    print("portofelul_meu", portofelul_meu)
    print("tranzactii: ", tranzactii)

    time.sleep(5)
