# TPC2: Jogo dos 21 fósforos

## Andreia Machado Cardoso a107279

## Resumo
O TPC2 consistiu no desenvolvimento do código em Python para o jogo dos 21 fósforos:

### O jogo

* No início do jogo, há 21 fósforos;
* Cada jogador (computador ou utilizador), pode tirar 1, 2, 3 ou 4 fósforos quando for a sua vez de jogar;
* Os jogadores jogam alternadamente;
* **Quem tirar o último fósforo perde!**

### O programa 

* O jogo deverá ter dois modos: o jogador joga em primeiro lugar e o computador começa a jogar em segundo lugar e, no segundo modo, o computador começa em primeiro; 
* Quando o computador começa a jogar em segundo lugar, deve ganhar sempre o jogo;
* Quando o computador começa a jogar em primeiro lugar, se o utilizador cometer um erro de cálculo, o computador deverá passar para a posição de vencedor e ganhar o jogo.


## Resultados
```python
import random

def jogo_21fosforos():
    fosforos = 21
    print("=== Jogo dos 21 fósforos ===")
    print("Quem tirar o último fósforo perde!")
    
    modo = int(input("Escolha o modo: 1 - Jogador começa / 2 - Computador começa: "))
    
    if modo == 1:
        turno = "jogador"
    else:
        turno = "computador"
    
    while fosforos > 0:
        print(f"\nFósforos restantes: {fosforos}")
        
        if turno == "jogador":
            retirar = int(input("Quantos fósforos deseja retirar (1 a 4)? "))
            while retirar < 1 or retirar > 4 or retirar > fosforos:
                retirar = int(input("Escolha inválida. Digite entre 1 e 4, sem ultrapassar o total: "))
            print(f"Você retirou {retirar} fósforos.")
            fosforos = fosforos - retirar
            if fosforos == 0:
                print("Você tirou o último fósforo... Você perdeu!")
                return
            turno = "computador"
        else:
            if modo == 1:
                # Computador joga em segundo - faz com que a soma dos fósforos retirados em cada ronda seja 5
                retirar = 5 - retirar  
                if retirar > fosforos:
                    retirar = min(4, fosforos)
            else:
                # Computador começa - joga "normal", tentando explorar erros de cálculo do jogador
                resto = fosforos % 5
                if resto == 0:
                    retirar = random.randint(1, min(4, fosforos))
                else:
                    retirar = resto
            
            print(f"Computador retira {retirar} fósforos.")
            fosforos = fosforos - retirar
            if fosforos == 0:
                print("O computador tirou o último fósforo... O computador perdeu, você venceu!")
                return
            turno = "jogador"

# Executar jogo
jogo_21fosforos()

