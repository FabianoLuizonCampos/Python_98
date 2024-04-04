# Leitura de Arquivos

def main():

    #Leitura de arquivo utilizando o modo r - read
    # Caminho absoluto
    # arquivo = open("E:\\senai-maua\\PythonMaterial\\Python_98\\Arquivos\\texto.txt", "r")
    
    # Caminho do arquivo relativo
    # arquivo = open("\\Arquivos\\texto.txt", "r")

    arquivo = open("texto.txt", "r")

    # if arquivo.mode == 'r': # Verificação se o arquivo existe / leitura
    #     conteudo = arquivo.read()
    #     print(conteudo)

    if arquivo.mode == 'r':
        linhas = arquivo.readlines() # readlines ler linhas individualmente 
                                     # e criar uma lista com cada linha
        # print(linhas)
        for l in linhas:
            print(l)

    arquivo.close()

if __name__ == "__main__":
    main()