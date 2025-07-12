import os
import time

while True:
    os.system("cls" if os.name == "nt" else "clear")

    nome = input("Digite seu nome (para encerrar basta dar ENTER: ")

    if nome:
        print(f"Olá, {nome}! Seja bem-vindo(a)!")
        time.sleep(1)
    else:
        print("Que pena... Tchau!")
        break
