# esse script faz o cálculo dos tipos de média
from  mediacalc import mediasimples, suavizacaoex # importa funções externas
from os import system

def mainf():
    get_i = int(input("Qual Escolha uma opção:\n(1)Média Moda Simples\n(2)Suavização Exponencial\n>>>"))# menu
    list_op = [1,2] # lista de opções disponíveis

    if  get_i == 1:
        periodo = int(input("Quantidade de periodos?: ")) # recebe quantidade de periodos

        print(f"Digite os dados dos {periodo} ultimos periodos.\n")

        x = 1
        v = [] # lista vazia

        while x <= periodo: # loop para pegar todos os dados referente a quantidade de periodos, armazenando em uma lista

            p = float(input(f"periodo {x}:"))# recebe o input de dados de cada periodo

            v.append(p) # cada vez que o loop se repete, um dado é armazenado na lista

            x += 1 # adiciona 1 unidade inteira a variavel x para quebrar a condicional do loop (x <= periodo)

        mediasimples(v)# pega o elementos da lista 
        

    elif get_i == 2:
        demanda = int(input("Demanda prevista: "))# recebe demanda prevista
        d_real = int(input("Demanda real: "))# recebe demanda real

        suavizacaoex(demanda, d_real)# pega demanda prevista e real e utiliza na função

    elif get_i == 3:
        print("em desenvolvimento...")

    elif get_i == 4:
        print("em desenvolvimento...")

    elif get_i is not list_op or get_i != type(get_i):
        print("Algo deu errado, tente novamente...")
        print(type(get_i))
        system("pause")
        mainf()

mainf()