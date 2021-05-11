# Ex1: Neste caso quando ele acha o teste que der verdadeiro ele pula para o final da estrutura
a = 10
b = 20
c = 5
res = 0

if a > b:
    res = a
elif a < b:
    res = b
elif a > c:
    res = c
else:
    res = a + b + c

print(res)

# Ex2: Neste caso ele testa todas as opcoes
a = 10
b = 20
c = 5
res = 0

if a > b:
    res = a
if a < b:
    res = b
if a > c:
    res = c
else:
    res = a + b + c

print(res)

# Ex3:
clima = "chuva"
dinheiro = 600
lugar = " "

if clima == "sol" and dinheiro > 300 and dinheiro <= 500:
    lugar = "clube"
elif clima == 'sol' and dinheiro > 500 and dinheiro <= 1000:
    lugar = 'clube'
elif clima =="chuva" and dinheiro < 600:
    lugar = 'casa da minha mãe'
elif clima == 'chuva' and dinheiro >=600:
    lugar = 'boate '
else:
    lugar = "cinema"

print('Vou a/o ', lugar)

