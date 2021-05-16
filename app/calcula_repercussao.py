# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:20:21 2021

@author: augusto.pavao
"""
"""
Baseados em dados de análise de anúncios anteriores, a agência tem os seguintes dados:
    
a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
cada compartilhamento nas redes sociais gera 40 novas visualizações.
30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
o mesmo anúncio é compartilhado no máximo 4 vezes em sequência

(1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)


Crie um script em sua linguagem de programação preferida que receba o valor investido em reais e retorne uma projeção aproximada
 da quantidade máxima de pessoas que visualizarão o mesmo anúncio (considerando o anúncio original + os compartilhamentos)
"""


"""
Esquema

n_cliks = 12 * ([n_vis_0 = Reais * 30]/100)

n_comp = 3 * (n_cliks/20)

n_new_vis = 40* n_comp

n_vis_der (por etapa) = n_vis_0 + n_new_vis

fazer função n_vis_der()


FOI CONSIDERADA APENAS A parte INTEIRA DAS DIVISÕES

"""
import math

def calcula_vis_derivadas(vis_ini):
    temp = math.floor(vis_ini / conv_clicks_by_vis[0]) * conv_clicks_by_vis[1]
    temp = math.floor(temp / conv_comp_by_clicks[0]) * conv_comp_by_clicks[1] 
    new_vis = math.floor(temp / conv_new_vis_by_comp[0])  * conv_new_vis_by_comp[1]
    
    return new_vis


def calcula_vis_inicial(valor_inv,conv_vis_by_reais):
    n_vis = math.floor(valor_inv / conv_vis_by_reais[0]) * conv_vis_by_reais[1]
    
    return n_vis

# Parâmetros históricos e restrições do problema

cota_vis = 1 # cota em reais que gera visualizações
vis_by_cota = 30    # número de visualizações geradas por uma cota
                    # em reais
conv_vis_by_reais = [cota_vis,vis_by_cota] # lista que agrega os dois fatores


cota_cliks = 100 # cota de visualizações que gera cliks
cliks_by_cota = 12 # número de cliks gerados por uma cota de
                    # visualizações
conv_clicks_by_vis =  [cota_cliks,cliks_by_cota] # lista que agrega os dois fatores


cota_comp = 20
comp_by_cota = 3 # número de compartilhamentos gerados por uma cota de
                    # cliks
conv_comp_by_clicks =  [cota_comp,comp_by_cota] # lista que agrega os dois fatores


cota_new_vis = 1
new_vis_by_cota  = 40 # número de novas visualizações geradas por uma cota de
                    # clikscompartilhamentos
conv_new_vis_by_comp =  [cota_new_vis,new_vis_by_cota] # lista que agrega os dois fatores


n_comp = 4 # númeor ma´ximo de compartilhamentos 


# Variáveis

Vis_por_comp = []   # lista que armazena as visualizações iniciais em cada
                    # etapa dos compartilhamentos

    
def main(valor_inv):
    # Calcula Vis_por_comp[0]: a quantidade de visualizações iniciais geradas
    # diretamente pelo investimento    
    for comp in range(n_comp): # laço que simula os compartilhamentos
        Vis_por_comp.append(0) # cria a linha na lista e inicia com valor  '0'
        if comp == 0:
            Vis_por_comp[comp] = calcula_vis_inicial(valor_inv,conv_vis_by_reais)
            continue # passa para o próximo passo do laço (para comp > 0)
        else:
            Vis_por_comp[comp] = calcula_vis_derivadas(Vis_por_comp[comp-1])
    
    for comp in range(n_comp):
        print('comp = ',comp,' :  ',Vis_por_comp[comp])

if __name__ == "__main__":
    main()




