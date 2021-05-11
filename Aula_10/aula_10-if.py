#EX1:
a = True

if a :
    print("Tem conteudo")
else:
    print('Não tem conteúdo')
print("Fim do programa")

# EX2:

b = False
if b :
    print("Tem conteudo")
else:
    print('Não tem conteúdo')
print("Fim do programa")

# EX3:

a = 10
b = 5
if a > b:
    print("Verdadeiro")
else:
    print("Falso")

# Ex4:
a = 10
b = 5
operacao = '+'
res = 0

if operacao == '+':
    res = a + b
print("Operação", operacao, ": ", res)

#EX5:
a = 10
b = 5
op = "-"
res = 0

if op =="+":
    res = a + b
if op =='-':
    res = a - b
if op == '*':
    res = a * b
if op == '/':
    res = a/b
print(str(a) + op + str(b) + ' = ' + str(res))