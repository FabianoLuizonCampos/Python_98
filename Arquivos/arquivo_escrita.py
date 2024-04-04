def main():

    arquivo = open("novo.txt", "a+")

    arquivo.write("\n")
    arquivo.write("Jairo Candido")
    arquivo.write("\n")
    arquivo.write("SENAI")

    arquivo.close()


if __name__ == "__main__":
    main()