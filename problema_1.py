# Un banco necesita controlar el acceso a cuentas bancarias y para ello desea hacer un programa de prueba en Java que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado.
# Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:
# 40 procesos que ingresan 100
# 20 procesos que ingresan 50
# 60 que ingresen 20.
# De la misma manera se desean lo siguientes procesos que retiran cantidades.
# 40 procesos que retiran 100
# 20 procesos que retiran 50
# 60 que retiran 20.
# Se desea comprobar que tras la ejecución la cuenta tiene exactamente 100 euros, que era la cantidad de la que se disponía al principio.


import time
import random
import subprocess
import signal
import multiprocessing
import itertools
import collections
from multiprocessing import Pool

class CuentaBancaria:
    def __init__(self):
        self.cantidad = 100

    def ingresar(self, cantidad):
        self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad



if __name__ == '__main__':
    cuenta = CuentaBancaria()
    with Pool(40) as p:
        p.map(cuenta.ingresar, [100]*40)

    with Pool(20) as p:
        p.map(cuenta.ingresar, [50]*20)

    with Pool(60) as p:
        p.map(cuenta.ingresar, [20]*60)

    with Pool(40) as p:
        p.map(cuenta.retirar, [100]*40)

    with Pool(20) as p:
        p.map(cuenta.retirar, [50]*20)

    with Pool(60) as p:
        p.map(cuenta.retirar, [20]*60)

    print(cuenta.cantidad)
