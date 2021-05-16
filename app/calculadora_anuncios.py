# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:20:21 2021

@author: augusto.pavao
"""
"""
Este módulo recebe como entrada (argumento de sistema) o "valor total investido"
em um anúncio e retorna as quantidades máximas de visualizações, de cliques e 
de comaprtilhamentos que o anúncio poderá ter, armazenados no arquivo 
repercussaorepercussao.txt. 
Esse cálculo é feito a partir de dados de análise de anúncios anteriores feito
pela agência.
O arquivo parametros_reperc.xlsx contém esse dados, que podem ser então 
atualizados/modificados conforme o histórico da agência.

O valor do investimento de entrada é um passado na execução do módulo se 
executado individualemnte ou como parâmetro da função mais() se importado
de outro módulo, neste caso, como exemplo:

import calcuadora_anuncios as calc

...

reperc = []

inv_total = 100

reperc = calc.main(inv_total)

...
"""
import sys
import math
import pandas as pd

def calcula_vis_derivadas(vis_ini):
    global total_vis
    n_cliks = calcula_cliks(vis_ini)
    n_comp = calcula_comp(n_cliks)
    new_vis = math.floor(n_comp / conv_new_vis_by_comp[0])  * conv_new_vis_by_comp[1]
    total_vis += new_vis
    return new_vis

def calcula_vis_inicial(valor_inv,conv_vis_by_reais):
    global total_vis
    n_vis = math.floor(valor_inv / conv_vis_by_reais[0]) * conv_vis_by_reais[1]
    total_vis += n_vis
    return n_vis

def calcula_cliks(n_vis):
    global total_cliks
    n_cliks = math.floor(n_vis / conv_clicks_by_vis[0]) * conv_clicks_by_vis[1]
    total_cliks += n_cliks
    return n_cliks

def calcula_comp(n_cliks):
    global total_comp
    n_comp = math.floor(n_cliks / conv_comp_by_clicks[0]) * conv_comp_by_clicks[1]
    total_comp += n_comp
    return n_comp

# Parâmetros históricos e restrições do problema
# importados do arquivo parametros_reperc.xlxs

# Importação dos parâmetros de repercussão para dataframe Pandas
df_parametros = pd.read_excel('parametros_reperc.xlsx')

# Atribuição das variáveis dos parâmetros
# cota_vis: cota em reais que gera visualizações
cota_vis = df_parametros._get_value(0,'cota_vis')
# vis_by_cota: número de visualizações geradas por uma cota em reais
vis_by_cota = df_parametros._get_value(0,'vis_by_cota')
conv_vis_by_reais = [cota_vis,vis_by_cota] # lista que agrega os dois fatores

# cota_cliks: cota de visualizações que gera cliks
cota_cliks = df_parametros._get_value(0,'cota_cliks')
# cliks_by_cota: número de cliks gerados por uma cota de visualizações
cliks_by_cota = df_parametros._get_value(0,'cliks_by_cota')
conv_clicks_by_vis =  [cota_cliks,cliks_by_cota] # lista que agrega os dois fatores

# cota_comp: cota de cliks que gera compartilhamentos
cota_comp = df_parametros._get_value(0,'cota_comp')
# comp_by_cota: número de compartilhamentos gerados por uma cota de cliks
comp_by_cota = df_parametros._get_value(0,'comp_by_cota')
conv_comp_by_clicks =  [cota_comp,comp_by_cota] # lista que agrega os dois fatores


# cota_new_vis: cota de compartilhamentos que gera novas visualizações
cota_new_vis = df_parametros._get_value(0,'cota_new_vis')
# new_vis_by_cota: número de novas visualizações geradas por uma cota de
                    # compartilhamentos
new_vis_by_cota = df_parametros._get_value(0,'new_vis_by_cota')
conv_new_vis_by_comp =  [cota_new_vis,new_vis_by_cota] # lista que agrega os dois fatores

# max_comp: número máximo de compartilhamentos 
max_comp = df_parametros._get_value(0,'max_comp')


# Variáveis

Vis_por_comp = []   # lista que armazena as visualizações iniciais em cada
                    # etapa dos compartilhamentos

    
def calcula_reperc(valor_inv):
    # Calcula Vis_por_comp[0]: a quantidade de visualizações iniciais geradas
    # diretamente pelo investimento    

    for comp in range(max_comp): # laço que simula os compartilhamentos
        Vis_por_comp.append(0) # cria a linha na lista e inicia com valor  '0'
        if comp == 0:
            Vis_por_comp[comp] = calcula_vis_inicial(valor_inv,conv_vis_by_reais)
            continue # passa para o próximo passo do laço (para comp > 0)
        else:
            Vis_por_comp[comp] = calcula_vis_derivadas(Vis_por_comp[comp-1])
    
def main(valor_inv):
    global total_vis, total_cliks, total_comp
    total_vis = 0
    total_cliks = 0
    total_comp = 0
    #valor_inv = 100
    calcula_reperc(valor_inv)

    return [int(total_vis),int(total_cliks),int(total_comp)]

if __name__ == '__main__':
    valor_inv = float(sys.argv[1])
    reperc = main(valor_inv)
    with open("./repercussao.txt","w") as file_r:
        print('Dados de repercussão do anúncio:',file=file_r)
        print(file=file_r)
        print('Valor investido: ',valor_inv,file=file_r)
        print('Número máximo de visualizações esperado: ',total_vis,file=file_r)
        print('Número máximo de cliques esperado: ',total_cliks,file=file_r)
        print('Número máximo de compartilhamentos esperado: ',total_comp,file=file_r)
       
