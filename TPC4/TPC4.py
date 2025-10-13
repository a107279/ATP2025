def listar(cinema):
    print("----------Lista de Filmes--------")
    i = 1
    for elem in cinema:
        print(f"Sala{i} : Filme {elem[2]}")
        i = i + 1
    print("---------------------------------")
    return

def disponivel(cinema,filme,lugar):
    cond=True
    for elem in cinema:
        if elem[2] == filme:
            if lugar in elem[1][:]:
                cond = False
    return cond

def vendebilhete(cinema,filme,lugar):
    for elem in cinema:
        if elem[2] == filme:
            if lugar not in elem[1][:]:
                elem[1].append(lugar)
                print(f"Bilhete vendido para o lugar {lugar} do filme '{filme}'.")
            else:
                print(f"O lugar {lugar} já está ocupado.")
    return cinema

def listardisponibilidades(cinema):
    print("----------Lista de Disponibilidades--------")
    for elem in cinema:
        nlugaresdisp =  elem[0] - len(elem[1])
        print(f"Filme: {elem[2]} :: Nº de lugares disponíveis: {nlugaresdisp}")
    print("-------------------------------------------")
    return

def inserirSala(cinema, sala):
    _, _, novo_filme = sala
    for elem in cinema:
        if elem[2] == novo_filme:
            print(f"Já existe uma sala a exibir '{novo_filme}'. Não foi adicionada.")
            return cinema
    cinema.append(sala)
    print(f"Sala adicionada: {novo_filme} ({sala[0]} lugares).")
    return cinema


def menu(cinema):
    cond = True
    opcoes = ("1" , "2" , "3" , "4" , "5") 
    while cond:
        print(""" 
        ---------------Gestão de um Cinema-------------
        (1) Listar todos os filmes
        (2) Listar a disponibilidade das salas dos filmes
        (3) Vender bilhetes para um filme
        (4) Adicionar uma nova sala
        (5) Sair
        """)

        
        escolha = input("Escolha a sua opção introduzindo um número da lista:")

        if escolha in opcoes:

            if escolha == "1":
                listar(cinema)
            
            if escolha == "2":
                listardisponibilidades(cinema)
                
            elif escolha == "3":
                filme = input("Introduza o nome do filme: ")
                lugar = int(input("Introduza o número do lugar: "))
                if disponivel(cinema, filme, lugar):
                    vendebilhete(cinema, filme, lugar)
                else:
                    print("Lugar não disponível ou filme inexistente.")

            elif escolha == "4":
                nlugares = int(input("Introduza o número total de lugares da nova sala: "))
                filme = input("Introduza o nome do filme a exibir: ")
                nova_sala = (nlugares, [], filme)
                inserirSala(cinema, nova_sala)
            
            elif escolha == "5":
                print("Escolheu a opção de sair. Até à próxima!")
                cond = False
        else:
            print("Opção inválida. Por favor, escolha outra opção.")


sala1 = (150, [17,20,21], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = [sala1, sala2]

menu(cinema1)