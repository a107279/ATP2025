# TPC3: Aplicação para manipulação de listas de inteiros

## Andreia Machado Cardoso a107279

## Resumo
O TPC3 consistiu na criação de uma aplicação em Python que coloca no monitor o seguinte menu:

    * (1) Criar Lista 
    * (2) Ler Lista
    * (3) Soma
    * (4) Média
    * (5) Maior
    * (6) Menor
    * (7) estaOrdenada por ordem crescente
    * (8) estaOrdenada por ordem decrescente
    * (9) Procura um elemento
    * (0) Sair
- O utilizador irá escolher uma das opções introduzindo o número correspondente;
- Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu;
- Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.

* No desenvolvimento da aplicação deverá ter em atenção o seguinte:
    - A aplicação terá uma variável interna para guardar uma lista de números;
    - Na opção 1, deverá ser criada uma lista de números aleatórios entre 1 e 100 que será guardada na variável interna;
    - Na opção 2, deverá ser criada uma lista com números introduzidos pelo utilizador, que será guardada na variável interna;
    - Nestas primeiras opções, se a variável interna já tiver uma lista, esta será sobreposta/apagada pela nova lista;
    - Na opção 3, será calculada a soma dos elementos na lista no momento;
    - Na opção 4, será calculada a média dos elementos na lista no momento;
    - Na opção 5, será calculado o maior elemento da lista no momento;
    - Na opção 6, será calculado o menor elemento da lista no momento;
    - Na opção 7, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem crescente;
    - Na opção 8, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem decrescente;
    - Na opção 9, a aplicação irá procurar um elemento na lista, se o encontrar deverá devolver a sua posição, devolverá -1 se o elemento não estiver na lista;
    - Se o utilizador selecionar a opção 0, a aplicação deverá terminar mostrando a lista que está nesse momento guardada.








```python
# Definir o Menu
def Menu():
    print("----------------- MENU -----------------")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(10) Sair")
    print("----------------------------------------")

# Definir as funções
def Criar_Lista():
    import random
    N = int(input("Quantos números deseja que tenha a sua lista?"))
    lista = []
    i = 0
    while i < N:
        x = random.randint(1,100)
        lista.append(x)
        i = i + 1
    return lista


def Ler_Lista():
    lista = []
    entrada = input("Introduza um número da sua lista. Quando não desejar introduzir mais números, escreva <<fim>>.")
    while entrada != "fim":
        x = int(entrada)
        lista.append(x)
        entrada = input("Introduza um número da sua lista. Quando não desejar introduzir mais números, escreva <<fim>>.")
    return lista


def Soma_Lista(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    return f"A soma dos elementos da lista é: {soma}"


def Media_Lista(lista):
    soma = Soma_Lista(lista)
    media = 0
    if len(lista) != 0:
        media = soma/len(lista)
    return f"A média dos elementos da lista é: {media}"


def Maior_Lista(lista):
    maior = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > maior:
            maior = lista [i]
        i = i + 1
    return f"O maior elemento da lista é: {maior}"


def Menor_Lista(lista):
    menor = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < menor:
            menor = lista [i]
        i = i + 1
    return f"O menor elemento da lista é: {menor}"


def Esta_Ordenada_Por_Ordem_Crescente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista [i+1]:
            return "Não, não está ordenada por ordem crescente."
    return "Sim, está ordenada por ordem crescente."


def Esta_Ordenada_Por_Ordem_Decrescente(lista):
    for i in range(len(lista) - 1):
        if lista[i] < lista [i+1]:
            return "Não, não está ordenada por ordem decrescente."
    return "Sim, está ordenada por ordem decrescente."


def Procurar_Elemento(lista):
    x = int(input("Que elemento deseja encontrar na lista?"))
    if x in lista:
        return f"Elemento encontrado na posição {lista.index(x)}."
    else: 
        return "-1: Elemento não encontrado"

#Definir o Main
def Main():
    lista = []
    cond = True
    while cond:
        Menu()
        opcao = input("Introduza a opção pretendida.")

        if opcao == "1":
            lista = Criar_Lista()
            print(lista)
            
        elif opcao == "2":
            lista = Ler_Lista()
            print(lista)
            
        elif opcao == "3":
            res = Soma_Lista(lista)
            print(res)
            
        elif opcao == "4":
            res = Media_Lista(lista)
            print(res)
            
        elif opcao == "5":
            res = Maior_Lista(lista)
            print(res)
            
        elif opcao == "6":
            res = Menor_Lista(lista)
            print(res)
            
        elif opcao == "7":
            res = Esta_Ordenada_Por_Ordem_Crescente(lista)
            print(res)
            
        elif opcao == "8":
            res = Esta_Ordenada_Por_Ordem_Decrescente(lista)
            print(res)
            
        elif opcao == "9":
            res = Procurar_Elemento(lista)
            print(res)
            
        elif opcao == "10":
            cond = False
            print("Até à próxima!")
        
        else:
            print("Resposta inválida. Por favor, insira um número entre 1 e 10.")

Main()
