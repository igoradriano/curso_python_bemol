num1 = num2 = res = 0
canal = "Canal Global"

print(canal)
def cn():
    global canal
    canal = "Canal Global assume um novo valor dentro da funcao"
    print(canal)

cn()
print(canal)

#-------------------
print("-------------")


def cn2():
    canal = "Canal Local da segunda funcao"
    print(canal)

cn2()