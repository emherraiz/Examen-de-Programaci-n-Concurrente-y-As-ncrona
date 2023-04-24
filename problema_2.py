# Se desea simular los posibles beneficios de diversas estrategias de juego en un casino. La ruleta francesa es un juego en el que hay una ruleta con 37 números (del 0 al 36). Cada 3000 milisegundos el croupier saca un número al azar y los diversos hilos apuestan para ver si ganan. Todos los hilos empiezan con 1.000 euros y la banca (que controla la ruleta) con 50.000. Cuando los jugadores pierden dinero, la banca incrementa su saldo.
# Se puede jugar a un número concreto. Habrá 4 hilos que eligen números al azar del 1 al 36 (no el 0) y restarán 10 euros de su saldo para apostar a ese ese número. Si sale su número su saldo se incrementa en 360 euros (36 veces lo apostado).
# Se puede jugar a par/impar. Habrá 4 hilos que eligen al azar si apuestan a que saldrá un número par o un número impar. Siempre restan 10 euros para apostar y si ganan incrementan su saldo en 20 euros.
# Se puede jugar a la «martingala». Habrá 4 hilos que eligen números al azar. Elegirán un número y empezarán restando 10 euros de su saldo para apostar a ese número. Si ganan incrementan su saldo en 360 euros. Si pierden jugarán el doble de su apuesta anterior (es decir, 20, luego 40, luego 80, y así sucesivamente)
# La banca acepta todas las apuestas pero nunca paga más dinero del que tiene.
# Si sale el 0, todo el mundo pierde y la banca se queda con todo el dinero.

import random
import time
import threading
import multiprocessing
import itertools
import collections
from multiprocessing import Pool

class Banca:
    def __init__(self):
        self.cantidad = 50000
        self.numero = 0

    def pierde(self, cantidad):
        self.cantidad -= cantidad

    def generar_numero(self):
        self.numero = random.randint(0, 36)

    def get_numero(self):
        return self.numero

    def ganar(self, cantidad):
        self.cantidad += cantidad

    def quiebra(self):
        if self.cantidad <= 0:
            return True
        else:
            return False

class Jugador(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.cantidad = 1000

    def run(self):
        while True:
            if self.cantidad <= 0:
                break
            else:
                self.jugar()

    def jugar(self, banca, tipo_de_juego):
        # Realiza la apuesta.
        self.cantidad -= 10
        banca.ganar(10)

        # Genera el número.
        numero = random.randint(1, 36)

        # Según el tipo de juego, se realiza la apuesta.
        if tipo_de_juego == 'numero':
            if banca.get_numero() == numero:
                if not banca.quiebra():
                    self.cantidad += 360
                    banca.pierde(360)

                else:
                    # Detenemos el juego y todos los procesos.
                    print('La banca se ha quedado sin dinero. Fin del juego.')
                    exit()


        elif tipo_de_juego == 'par_impar':
            if banca.get_numero() % 2 == 0:
                self.cantidad += 20

        elif tipo_de_juego == 'martingala':
            if banca.get_numero() == numero:
                self.cantidad += 360
            else:
                self.cantidad -= 20




if __name__ == '__main__':


