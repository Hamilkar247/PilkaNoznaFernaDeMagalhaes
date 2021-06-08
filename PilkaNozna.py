import random
import logging

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
        self.adversario = self.randomizacao(numeroAdversario, 0, 10)

    def printEquipa(self):
        print("------------")
        print(self.nomeEquipa)
        print(self.adversario)

    def escolherAdversario(self):
        escolher = random.randint(0, self.numeroAdversario-1)
        #print(f"escolher: {escolher}")
        return self.adversario[escolher]

class Evento():

    def chuter(self, offensivo, defensivo):  #strzał
        print(f"Akcja dla zespolu {offensivo.nomeEquipa}")
        variavel = random.randint(-10,10)
        ataque=offensivo.escolherAdversario()
        advocate=defensivo.escolherAdversario()
        if variavel+ataque>advocate:
            print("GOOOL")
        else:
            print("Chyba celował panu Bogu w okno")


    def __init__(self):
        pass

def partida(primeiro, segundo):
    evento = Evento()
    primeiro.printEquipa()
    segundo.printEquipa()
    iniciativa = random.randint(1,2)
    if iniciativa == 1:
         evento.chuter(primeiro, segundo)
         iniciativa = 0
    else:
         evento.chuter(segundo, primeiro)
         iniciativa = 1

    numeroMinuto=0
    while numeroMinuto<3:
        numeroMinuto = numeroMinuto + 1
        print(f"numeroMinuto: {numeroMinuto}")
        primeiro.escolherAdversario()

        if iniciativa == 1:
             evento.chuter(primeiro, segundo)
             iniciativa = 0
        else:
             evento.chuter(segundo, primeiro)
             iniciativa = 1


def main():
    WislaKrakow = Equipa("WislaKrakow", 5)
    LegiaWarszawa = Equipa("LegiaWarszawa", 5)
    partida(WislaKrakow, LegiaWarszawa)

if __name__ == "__main__":
    main()
