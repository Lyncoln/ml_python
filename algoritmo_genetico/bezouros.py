# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:02:26 2019

@author: Lyncoln
"""


from random import randint,choices
import pandas as pd


def fitnes(população):
    return(list(map(lambda x: (1 - sum(x)/(3*255)), populacao)))

def inicia(num):
    populacao = []
    for i in range(num+1):
        indv = [randint(0,255),randint(0,255),randint(0,255)]
        populacao.append(indv)
    return populacao
        
def escolhe(populacao, fitnes,n):
    soma = sum(fitnes)
    pesos = list(map(lambda x: x/soma, fitnes))
    escolhidos = choices(populacao, pesos, k = n)
    return(escolhidos)
    
    
def escolhe2(populacao,fitnes,n):
     x = pd.DataFrame({"pop":populacao,"fit":fitnes})
     x = x.sort_values(by = "fit", ascending=True)
     x = x.reset_index(drop=True)
     x.index += 1
     x = x.assign( peso = x.index / sum(x.index))
     escolhidos = choices(x["pop"], x["peso"], k = n)
     return(escolhidos)
     
     
     
    
def crossover(escolhidos):
    filho = []
    pai = escolhidos[0]
    mae = escolhidos[1]
    pos = randint(1,2)
    for i in pai[:pos]:
        filho.append(i)
    for i in mae[:-pos]:
        filho.append(i)
    return(filho)
    
def mutacao(filho):
    pos = randint(0,2)
    filho[pos] = filho[pos] + randint(-10,10)
    if(filho[pos] < 0):
        filho[pos] = 0
    if(filho[pos] > 255):
        filho[pos] = 255
    return(filho)
    
    


    
    


populacao = inicia(29)

for k in range(1000):
    fit = fitnes(populacao)
    pais = escolhe2(populacao, fit,2)
    filhos = []
    for i in range(30):
        genoma = (crossover(pais))
        filhos.append(mutacao(genoma))
    populacao = filhos


