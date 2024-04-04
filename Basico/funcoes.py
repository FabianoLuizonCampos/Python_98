# Funções (definicao simploria): 
#  - Parte do codigo que eu quero que aconteca varias vezes
#  - Módulo separado do modulo principal

# FUNCAO CALCULO IMC    
def calcularIMC(peso, altura):

    imc = peso / (altura ** 2)
    imc = round(imc,2)

    return imc


# FUNCAO PRINCIPAL
def main():
    
    nome = input("Olá, qual é seu nome: ")
    
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = calcularIMC(peso, altura)
    

    print(f" {nome} seu IMC é {imc}")


# CONDICAO PARA EXECUTAR A FUNCAO PRINCIPAL
if __name__ == "__main__":
    main()