#!/usr/bin/python3

pergunta = int(input("Me diga quantos números pares você quer ver: "))


# Estrutura de list comprehension
dobro = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro)

# Versão normal
dobros = []
for i in range(10):
    if i % 2 == 0:
        dobros.append(i * 2)
print(dobros)
