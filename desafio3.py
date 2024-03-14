lista_de_lanches = ["BIG MAC", "MC CHEDDAR", "QUARTEIRAO", "BIG TASTY"]
lista_de_precos = [ 29.90, 27.90, 18.50, 35.60]

print("---- BEM VINDO AO MAC SENAI Maua -----")
opcao = int(input("Digite sua opcao de lanche:"))

print("Seu lanche escolhido foi ",lista_de_lanches[opcao - 1])
print("O valor do lanche e R$ ", lista_de_precos[opcao - 1])
