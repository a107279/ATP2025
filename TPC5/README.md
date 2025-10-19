# TPC5: Aplicação para gestão de alunos

## Andreia Machado Cardoso a107279

## Resumo
O TPC5 consistiu na criação de uma aplicação em Python para gestão de um conjunto de alunos de uma turma. Nessa aplicação é possível criar uma turma; inserir um aluno na turma; listar a turma; consultar um aluno por id; guardar a turma em ficheiro e carregar uma turma dum ficheiro.

## Resultados:
```python
import json

def criarTurma():
    turma = [("Ana", "A107260", [15.0, 17.0, 14.0]),
        ("Bruno", "A108734", [12.5, 13.0, 11.5]),
        ("Carla", "A107653", [18.0, 16.0, 19.0]),
        ("Duarte", "A107894", [14.5, 15.0, 13.5]),
        ("Eva", "A108304", [19.0, 18.5, 17.0])
    ]
    print("\nTurma criada com 5 alunos de exemplo!\n")
    return turma

def inserirAluno(turma):
    nome = input("Introduza o nome do aluno:")
    id = input("Introduza o id do aluno:")
    existe = False
    for elem in turma:
        if elem[1] == id:
            existe = True
    if not existe:
        notaTPC = float(input("Introduza a nota do TPC do aluno:"))
        notaProj = float(input("Introduza a nota do Projeto do aluno:"))
        notaTeste = float(input("Introduza a nota do Teste do aluno:"))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
        print(f"\nAluno {nome} inserido com sucesso!")
    else:
        print(f"\nJá existe um aluno como id {id}.\n")
    return turma

def listarTurma(turma):
    if turma: 
        print(f"------------Listagem de turma:------------")
        for elem in turma:
            print(f"\n Aluno: {elem[0]} | ID: {elem[1]} | Nota do TPC: {elem[2][0]}, Nota do Projeto: {elem[2][1]}, Nota do Teste: {elem[2][2]}")
    else: 
        print("\nA turma está vazia!\n")
    return

def consultarID(turma):
    id = input("Introduza o id do aluno que pretende consultar:")
    encontrado = False
    for elem in turma:
        if id == elem[1]:
            print(f"\n Aluno: {elem[0]} | ID: {elem[1]} | Nota do TPC: {elem[2][0]}, Nota do Projeto: {elem[2][1]}, Nota do Teste: {elem[2][2]}")
            encontrado = True
    if not encontrado:
        print(f"\nNão foi encontrado nenhum aluno com o id {id}.\n")
    return

def guardarTurma(turma):
    if turma:
        nome_fich = input("Introduza o nome do ficheiro para guardar a turma (ex: turma.json): ")
        turma_json = [list(aluno) for aluno in turma]
        f = open(nome_fich, "w", encoding="utf-8")
        json.dump(turma_json, f, ensure_ascii=False, indent=4)
        f.close()

        print(f"\nTurma guardada no ficheiro '{nome_fich}' com sucesso!\n")
    else:
        print("\nNão há turma para guardar.\n")


def carregarTurma():
    nome_fich = input("Introduza o nome do ficheiro da turma a carregar (ex: turma.json): ")

    f = open(nome_fich, "r", encoding="utf-8")
    turma_json = json.load(f)
    f.close()

    turma = [(a[0], a[1], a[2]) for a in turma_json]

    print(f"\nTurma carregada com sucesso a partir de '{nome_fich}'.\n")
    input("Pressione Enter para continuar...")
    return turma



def menu():
    turma = []
    cond = True
    opcoes = ("1" , "2" , "3" , "4" , "8", "9", "0") 
    while cond:
        print(""" 
        ---------------Gestão de Alunos-------------
        (1) Criar uma turma
        (2) Inserir um aluno na turma
        (3) Listar a turma
        (4) Consultar um aluno por id
        (8) Guardar a turma em ficheiro
        (9) Carregar uma turma dum ficheiro
        (0) Sair
        """)

        
        escolha = input("Escolha a sua opção introduzindo um número da lista:").strip()

        if escolha in opcoes:

            if escolha == "1":
                turma = criarTurma()
                
            
            elif escolha == "2":
                turma = inserirAluno(turma)
                
                
            elif escolha == "3":
                listarTurma(turma)

            elif escolha == "4":
                consultarID(turma)

            elif escolha == "8":
                guardarTurma(turma)
            
            elif escolha == "9":
                turma = carregarTurma()
                
            elif escolha == "0":
                print("\nEscolheu a opção de sair. Até à próxima!\n")
                cond = False
                
                
        else:
            print("Opção inválida. Por favor, escolha outra opção.")

menu()
