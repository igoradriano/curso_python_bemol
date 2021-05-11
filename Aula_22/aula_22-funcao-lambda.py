# Funcoes anonimas
soma = lambda a,b : a + b
mult = lambda a,b,c : (a+b)*c
print((lambda a,b: a - b)(3,44))   # Neste caso nem preciso declar nome, nem chamá-la, ele ja executa 

# Usando a funcao criada
c = soma(1,2)
print(c)
print(soma(1,2))
print(mult(1,2,3))


# Usando funcoes como parâmetro da funcao lambda
r = lambda x,func: x + func(x)      # r assume uma lambda que recebe um numero e uma funcao, onde essa funcao recebe x como argumento e soma-se ao valor do proprio x ou seja: x + f(x)
res =r(22,lambda x:x*x)  # agora passo o valor de x e uma nova funcao lambda que recebe x e multiplica por x
print("res: ",res) # printamos res

# Ex2:
a = lambda x,y,func:x + func(x,y)
result = a(22,10,lambda x,y:x*y*2)
print('Res:', result)