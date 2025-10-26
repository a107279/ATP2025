# TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
    # Data = (Int,Int,Int)
    # TempMin = Float
    # TempMax = Float
    # Precipitacao = Float

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

### 1.a) Calcula a temperatura média de cada dia, dando como resultado uma lista de pares: [(data, temperaturaMédia)]:
def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
            media = (dia[1] + dia[2]) / 2
            res.append((dia[0], media))
    return res

### 1.b) Define uma função para guardar uma tabela meteorológica num ficheiro de texto.
def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        registo = f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}\n"
        file.write(registo)
    file.close()
    return

### 1.c) Define uma função para carregar uma tabela meteorológica de um ficheiro de texto.
def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    # text = f.read()
    for linha in file:
        linha = linha.strip() # Tira os espaços em branco "" e "\n"
        campos = linha.split("|")
        data, tmin, tmax, prec = campos
        ano, mes, dia = data.split("-")
        res.append(((int(ano),int(mes),int(dia)), float(tmin), float(tmax), float(prec)))
    file.close()
    return res

### 1.d) Calcula a temperatura mínima mais baixa registada na tabela, dando como resultado esse valor:
def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for data,tmin,tmax,prec in tabMeteo:
        if tmin < minima:
            minima = tmin
    return minima

### 1.e) Calcula a amplitude térmica (diferença entre a temperatura máxima e a temperatura mínima) de cada dia, dando como resultado uma lista de pares: [(data, amplitude)]
def amplTerm(tabMeteo):
    res = []
    for data,tmin,tmax,prec in tabMeteo:
        amplitude = tmax - tmin
        res.append((data,amplitude))
    return res 

### 1.f) Calcula o dia em que a precipitação registada teve o seu valor máximo e indica esse valor, dando como resultado o par (data, valor):
def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    for data,tmin,tmax,prec in tabMeteo:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)

### 1.g) Define uma função que recebe uma tabela meteorológica e um limite `p` e retorna uma lista de pares [(data, precipitação)] correspondente aos dias em que a precipitação foi superior a `p`.
def diasChuvosos(tabMeteo, p):
    res = []
    for data,tmin,tmax,prec in tabMeteo:
        if prec > p:
            res.append((data,prec))
    return res

### 1.h) Define uma função que recebe uma tabela meteorológica e um limite `p` e retorna o maior número consecutivo de dias com precipitação abaixo desse limite.
def maxPeriodoCalor(tabMeteo, p):
    local_consec = 0
    global_consec = 0
    for data,tmin,tmax,prec in tabMeteo:
        if prec < p:
            local_consec = local_consec + 1
        else:
            if local_consec > global_consec:
                global_consec = local_consec
            local_consec = 0 
    if local_consec > global_consec:
        global_consec = local_consec           
    return global_consec

### 1.i) Define uma função que recebe uma tabela meteorológica e desenha os gráficos da temperatura mínima, máxima e de pluviosidade.
from matplotlib import pyplot as plt

def grafTabMeteo(t):
    x =[f"{data[0]}/{data[1]}/{data[2]}" for data, tmin, tmax, prec in t]
    y_min = [tmin for data, tmin, tmax, prec in t]
    y_max = [tmax for data, tmin, tmax, prec in t]
    precs = [prec for *_, prec in t]

    plt.plot(x,y_min, label="Temperatura Mínima (ºC)", color = "pink", marker = "o")
    plt.plot(x,y_max, label="Temperatura Máxima (ºC)", color = "purple", marker = "o")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

    plt.bar(x,precs, label="Pluviosidade (mm)", color = "c")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

    return

def menu():
    tabMeteo = tabMeteo1
    fnome = "meteorologia.txt"
    p = None
    cond = True
    while cond:
        print(""" 
        ---------------Tabela Meteorológica-------------
        (1) Calcular a temperatura média de cada dia
        (2) Guardar a tabela meteorológica num ficheiro de texto
        (3) Carregar a tabela meteorológica dum ficheiro de texto
        (4) Calcular a temperatura mínima mais baixa
        (5) Calcular a amplitude térmica de cada dia
        (6) Calcular o dia em que a precipitação foi máxima e o seu valor
        (7) Calcular os dias em que a precipitação foi maior que um valor p
        (8) Calcular o maior número consecutivo de dias com precipitação abaixo de um valor p
        (9) Desenhar os gráficos da temperatura mínima, máxima e de pluviosidade
        (0) Sair
        ------------------------------------------------
        """)

        
        opcao = input("Escolha a sua opção introduzindo um número da lista:")

    
        if opcao == "1":
            resultado = medias(tabMeteo)
            print(f"Temperatura média de cada dia: {resultado}")
            
        
        elif opcao == "2":
            guardaTabMeteo(tabMeteo,fnome)
            print(f"Tabela guardada em {fnome}")
            
            
        elif opcao == "3":
            tabMeteo = carregaTabMeteo(fnome)
            print(f"Tabela carregada: {tabMeteo}")

        elif opcao == "4":
            resultado = minMin(tabMeteo)
            print(f"Temperatura mínima mais baixa: {resultado}")

        elif opcao == "5":
            resultado = amplTerm(tabMeteo)
            print(f"Amplitude térmica de cada dia: {resultado}")
        
        elif opcao == "6":
            resultado = maxChuva(tabMeteo)
            print(f"Dia com precipitação máxima: {resultado}")
        
        elif opcao == "7":
            p = float(input("Introduza um valor para o limite p:"))
            resultado = diasChuvosos(tabMeteo,p)
            print(f"Dias com a precipitação maior que {p}: {resultado}")

        elif opcao == "8":
            p = float(input("Introduza um valor para o limite p:"))
            resultado = maxPeriodoCalor(tabMeteo,p)
            print(f"Nº máximo de dias consecutivos com precipitação abaico de {p}: {resultado}")
               
        elif opcao == "9":
            if tabMeteo:
                grafTabMeteo(tabMeteo)
            else:
                print("Carregue ou insira dados na tabela antes de criar gráficos.")

        elif opcao == "0":
            print("\nEscolheu a opção de sair. Até à próxima!\n")
            cond = False
                         
        else:
            print("Opção inválida. Por favor, escolha outra opção.")

menu()