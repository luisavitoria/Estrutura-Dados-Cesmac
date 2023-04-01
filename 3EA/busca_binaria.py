# Lista de funcionários da empresa
funcionarios = [
  [1001, "João Silva", "123.456.789-00"],
  [1025, "Maria Santos", "234.567.890-11"],
  [1256, "José Almeida", "345.678.901-22"],
  [1132, "Ana Souza", "456.789.012-33"],
  [1006, "Pedro Costa", "567.890.123-44"],
  [1968, "Luciana Oliveira", "678.901.234-55"],
  [1457, "Fernando Pereira", "789.012.345-66"],
  [1224, "Mariana Dias", "890.123.456-77"],
  [1675, "Ricardo Mendes", "901.234.567-88"],
  [1475, "Juliana Ferreira", "012.345.678-99"],
  [1011, "Felipe Rodrigues", "123.456.789-00"],
  [1369, "Renata Lima", "234.567.890-11"],
  [1087, "Marcelo Santos", "345.678.901-22"],
  [1344, "Carla Almeida", "456.789.012-33"],
  [1921, "Bruno Souza", "567.890.123-44"],
  [1034, "Daniela Costa", "678.901.234-55"],
  [1288, "Roberto Oliveira", "789.012.345-66"],
  [1593, "Sandra Pereira", "890.123.456-77"],
  [1375, "Vitor Mendes", "901.234.567-88"],
  [1111, "Carlos Alberto", "875.236.857-78"],
]

#Para realizar uma busca binária deve-se primeiro ordenar a lista de funcionários:
def ordenacao_insercao(lista):
    N = len(lista)
    for i in range(1, N):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0] > atual[0]: #seleciona o primeiro elemento de cada vetor (matrícula)
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = atual
    return lista

#Algoritmo de busca binária:
def busca_binaria(lista, matricula):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio][0] == matricula:
            return "Matrícula: " + str(lista[meio][0]) + "\nNome: " + lista[meio][1] + "\nCPF: " + lista[meio][2]
        elif lista[meio][0] < matricula:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return "Funcionário não encontrado no sistema."

funcionarios_ordenados = ordenacao_insercao(funcionarios)
matricula = input("Digite a matrícula do funcionário: ")
resultado = busca_binaria(funcionarios_ordenados, int(matricula))
print(resultado)