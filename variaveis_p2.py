# Variável do tipo lista
lista_de_frutas = ["maçã", "banana", "laranja", "uva"]
salarios = [2200, 5600, 9000]

# Variável do tipo tupla
tupla_de_cores = ("vermelho", "azul", "verde", "amarelo")
carros = ("FIAT", "VW", "GM")

# Variável do tipo dicionario
dicionario_de_pessoas = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "Mauá"
}

# Exibir os valores das variávies
print("Minha lista de frutas:", lista_de_frutas)
print("Tupla de cores:", tupla_de_cores)
print("Dicionario de pessoas", dicionario_de_pessoas)

# Acessar elementos especificos 
print("A segunda fruta da minha lista eh:", lista_de_frutas[1])
print("O segundo elemento da minha tupla eh: ", tupla_de_cores[1])

print("A idade de", dicionario_de_pessoas["nome"], " eh ", 
      dicionario_de_pessoas["idade"])