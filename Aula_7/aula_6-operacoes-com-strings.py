curso = '      Curso de Python'
print(curso)


for n in curso:
    print(n)

# Imprimindo parte da string
print(curso[9:15])

# Imprimindo o tamanho da string
print("Tamanho: " + str(len(curso)))
print(f'Tamanho: {len(curso)}')

# Método strip para remover espaços antes e depois da string
print(curso.strip())
print("Tamanho: "+ str(len(curso)))
print("Tamanho: "+ str(len(curso.strip())))


# Funcao lower (tudo minusculo)
print(curso.lower().strip())

#Funcao upper (tudo maiusculo)
print(curso.upper().strip())

# Funcao replace (substituit uma string ou carater)
print(curso.replace("Python","C#").strip())

#Funcao Split (subdivide a string)
a = curso.strip().split(" ")
print(a[2])
# para este exemplo retiramos os espaços antes e depois com o strip, depois colocamos o resultado em a, porem ele envia em forma de lista, logo, impimimos apenas o terceiro valor da lista a.
print(curso.strip().split("o"))

# Funcao Join ( juntar)
a = "Eu te amo meu amor"
print(";".join(a))

a = a.split(' ')
print(" ".join(a))


# FUCNAO IN
res= 'Python' in curso
print(res)
# porem CUIDADO!!
res = 'Pyth' in curso
print(res) #tambem vai dar true


# EX: Usando o upper para pesquisar paralavras que nao se encontram igualmente digitadas
text = 'Curso de python'
palavra = 'python'
res = palavra.upper() in text.upper()
print(res)


# FUNCAO NOT IN
res = 'Python' not in curso
print(res)


# CONCATENANDO STRINGS
curso = "Curso de Python"
canal = "CFB Cursos"

res = curso + " " + canal
print(res)

#Ex2:
cidade = "Manaus"
dia = 15
mes = "Dezembro"
ano = 2019

data = str(15) + "/" + mes +"/" + str(ano)
print(data)

#PLACEHOLDERS (FORMAT)
data = '{}, {} de {} de {}'
print(data.format(cidade,dia,mes,ano))

print('{}, {} de {} de {}'.format(cidade, dia,mes,ano))

# CARACTERES DE SCAPE
# imprimir aspas, barra,contra-barra,enter,espaco

canal = 'CFB Cursos'
# Quebra de linha
data = '{}, {} de {}\n {} - {}'
print(data.format(cidade, dia,mes,ano,canal))
# Imprimir ASPAS
data = '{}, {} de {} \"{}\" {}'
print(data.format(cidade, dia,mes,ano,canal))

# Mais comuns
#\'   - aspas
# \"  - aspas duplas
# \n  - pular linha 
# \r  - enter
# \t  - tabulacao   
# \b  - backspace (volta um caractere)