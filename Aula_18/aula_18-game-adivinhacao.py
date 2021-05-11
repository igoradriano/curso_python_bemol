#Sistema sorteia um numero de 0 1 100 e vamos ter que adivinhar o numero que ele sorteou. Ao final vai me dar o numero de tentativas que tive que usar para acertar o numero.
import random
"""
num = random.randrange(0,10)
i = 0
t = []
tentativa = ''
while True:
    i+=1
    tentativa = int(input("Tente adivinhar o número: "))
    t.append(tentativa)
    if tentativa == num:
        print(f"Parabéns! Você acertou e precisou de {i} tentativas")
        break"""

# Outro Programa
num1 = 0; num2 = 100
num = random.randrange(num1,num2)
i = 0; r = 0; lista = []; t = 0
while True:
    t = int(input(f"Tente adivinhar um número entre {num1} e {num2}: "))
    while t < num1 or t > num2:
        t = int(input(f"Digite APENAS números entre {num1} e {num2}: "))
    i+=1
    while t in lista:
        print("Você já tentou esse número!")
        t = int(input("Tente outro: "))
        i+=1
        r+=1
    lista.append(t)
    if t == num:
        print(f"Parabéns! Você acertou e precisou de {i} tentativas e repetiu o mesmo número {r} vezes")
        break
    if t > num:
        print('Errou, o número é MENOR')
    else:
        print('Errou, o número é MAIOR')
        
        
