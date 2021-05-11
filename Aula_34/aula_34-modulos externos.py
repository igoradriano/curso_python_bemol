from canal import canal_nome
import canal as cn
canal_nome()
# import canal
# canal.canal__nome()


# from canal import jogador
print(cn.jogador['nome'])
print(cn.jogador['energia'])

import canal
res = dir(canal)
print(res) # mostra tudo que tem dentro de canal