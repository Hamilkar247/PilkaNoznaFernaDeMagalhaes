import random
import logging
from time import sleep

class Equipa():

    def randomizacao(self, contagemDeElementos, minimo, maximo):
        numero = 0;
        serie = []
        while(numero < contagemDeElementos):
            numero = numero + 1
            serie.append(random.randint(minimo, maximo))
        return serie

    def __init__(self, nomeEquipa, numeroAdversario):
        self.nomeEquipa = nomeEquipa
        self.numeroAdversario = numeroAdversario
        self.memberosEquipa = self.randomizacao(numeroAdversario, 0, 100)

    def printEquipa(self):
        print("------------")
        print(self.nomeEquipa)
        print(self.memberosEquipa)

    def nomeEquipaGet(self):
        return self.nomeEquipa

    def escolherAdversario(self):
        escolher = random.randint(0, self.numeroAdversario-1)
        #print(f"escolher: {escolher}")
        return self.memberosEquipa[escolher]

class Evento():

    def chuter(self, offensivo, defensivo):  #strzał
        print(f"Akcja dla zespolu {offensivo.nomeEquipa}")
        variavel = random.randint(-10,10)
        ataque=offensivo.escolherAdversario()
        advocate=defensivo.escolherAdversario()
        if variavel+ataque>advocate:
            print("GOOOL")
            return 1
        else:
            print("Chyba celował panu Bogu w okno")
            return 0

    def __init__(self):
        pass

def partida(primeiro, segundo):
    evento = Evento()
    primeiro.printEquipa()
    segundo.printEquipa()
    golPrimeiro=0
    golSegundo=0
    iniciativa = random.randint(1,2)
    if iniciativa == 1:
         evento.chuter(primeiro, segundo)
         iniciativa = 0
    else:
         evento.chuter(segundo, primeiro)
         iniciativa = 1

    numeroMinuto=0
    while numeroMinuto<90:
        numeroMinuto = numeroMinuto + 10
        print(f"numeroMinuto: {numeroMinuto}")
        primeiro.escolherAdversario()

        if iniciativa == 1:
             golPrimeiro = golPrimeiro + evento.chuter(primeiro, segundo)
             iniciativa = 0
        else:
             golSegundo = golSegundo + evento.chuter(segundo, primeiro)
             iniciativa = 1
        sleep(1)
    #contagem
    print("----------------")
    print("Koniec meczu")
    print(f"{primeiro.nomeEquipaGet()} : {segundo.nomeEquipaGet()}")
    print(f"{golPrimeiro} : {golSegundo}")


class AdministrarEquipa():

     def __init__(self, nomoEquipa):
         pass

def main():
    WislaKrakow = Equipa("WislaKrakow", 5)
    administrarWislaKrakow = AdministrarEquipa(WislaKrakow)
    LegiaWarszawa = Equipa("LegiaWarszawa", 5)
    partida(WislaKrakow, LegiaWarszawa)

if __name__ == "__main__":
    main()

