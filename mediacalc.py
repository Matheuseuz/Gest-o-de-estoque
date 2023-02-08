from os import system

def mediasimples(lista):#função que calcula media simples
    
    mms = sum(lista) / len(lista) # soma a lista e divide pela quantidade de elementos existentes

    print("aplicando a formula: dados de cada periodo / numero de periodos")
    print(f"Mediasimples: {mms:.2f}")

    system("pause")

def suavizacaoex(pt,rt): #função que faz a suavização exponencial
    a = (pt - rt) / rt
                                # formula da suavização exponencial
    p = a * rt + (1-a) * pt

    print(f"Previsão para o próximo periodo: {p:.0f}")# :.0f para manter sem ponto flutuante, arredondando o numero para inteiro
    system("pause")
