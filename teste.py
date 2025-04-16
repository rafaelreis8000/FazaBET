from os import system
from random import choice
from time import sleep
from itertools import cycle

lista = ['tigrinho','tourinho','coelhinho','pandinha','dragaozinho']

for i in range(10):
    for value in lista:
        print(value)
        sleep(0.1)
        system('cls')