# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   1. O aluno deverá digitar 3 notas através do teclado
#   2. Seu programa deverá calcular a média das notas    
#   3. A partir da média, verificar qual situação o aluno se encontra 
# conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   4. Não será permitido médias acima de 100 e abaixo de zero
#   5. Caso isso ocorrá o aluno deverá ser informado sobre um erro de digitação
#   6. Mostrar na tela para o aluno a situação final baseado na nota digitada.

#   7. Acrescente no desafio anterior a frequencia de no minimo 75% para ser aprovado
#   8. O aluno pode ser aprovado se ele recebeu uma dispensa da disciplina

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

frequencia = int(input("Digite sua frequencia: "))

dispensa = input("Você possui dispensa da disciplina (S/N):")

if dispensa == 'S' or dispensa == 's':
    esta_dispensado = True
else:
    esta_dispensado = False

media = (nota1 + nota2 + nota3) / 3
media = round(media, 2)

if not esta_dispensado:
    if media >= 0 and media <= 100 and frequencia >= 75:
        if media >= 70:
            print("Aprovado")
        elif media >= 40 and media < 70:
            print("Exame")
        else:
            print("Reprovado")
        
        print("Sua media foi: ", media)
    elif media >= 0 and media <= 100 and frequencia < 70:
        print("Reprovado, frequencia menor que 75%")
    else:
        print("Erro no valor da media, calcule novamente")
else:
    print("Você esta aprovado por dispensa")