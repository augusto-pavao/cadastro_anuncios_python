# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:40:46 2021

@author: augusto.pavao
"""

import tkinter as tk

import tkinter.messagebox

import tkcalendar as tkcal

import pandas as pd

import webbrowser

from tempfile import NamedTemporaryFile

import datetime

import mysql.connector 

import calculadora_anuncios as calc

## 1. Definição das classes que utilizam o tkinter e geram a interface do usuário
class Principal:
    # Classe da tela principal do sistema utilizando tkinter
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, width = 1400, height = 300)
        self.titulo = tk.Label(self.frame, text="Sistema de Cadastro de Anúncios",
                               font=('Arial', 25))
        self.titulo.pack(padx=100,pady=50)

        self.button1 = tk.Button(self.frame, text = 'Cadastrar novo Anúncio',
                                 width = 100, font=('Arial', 15),bg='#1E90FF',
                                 command = self.w_cadastro)
        self.button1.pack(padx=100,pady=50)

        self.button2 = tk.Button(self.frame, text = 'Gerar Relatório',
                                 width = 100, font=('Arial', 15),bg='#00FA9A',
                                 command = self.w_relatorio)
        self.button2.pack(padx=100,pady=50)        
        self.frame.pack()

        self.button3 = tk.Button(self.frame, text = 'Sair do Sistema',
                                 width = 100, font=('Arial', 15),bg='#FA8072',
                                 command = self.close_windows)
        self.button3.pack(padx=100,pady=50)        
        self.frame.pack()
    
    # Classes das janelas  de cadastro e de relatório   
    def w_cadastro(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Cadastro(self.newWindow)
            
    def w_relatorio(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Relatorio(self.newWindow)

    def close_windows(self):
        self.master.destroy()

class Cadastro:
    # Classe da tela de cadastro
    # As variáveis que compõem o cadastro do anúncio são globais nesta classe
    global nome_anuncio, cliente, data_ini, data_fim, inv_dia
    nome_anuncio, cliente, data_ini, data_fim, inv_dia = '','','','',''
    
    def __init__(self, master):
        # Criação dos widgets da tela de cadastro
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.attributes('-topmost', True)
        self.label_titulo = tk.Label(self.master)
        self.label_titulo.configure(text="Cadastro de Anúncio",width=20,
                                    font=("bold", 20))
        self.label_titulo.grid(column=0, row=0) 
  
        self.label_nome_anuncio = tk.Label(self.master)
        self.label_nome_anuncio.configure(text="Nome do Anúncio",
                                          width=20,font=("bold", 10))
        self.label_nome_anuncio.grid(column=0, row=1) 
        self.entra_nome_anuncio = tk.Entry(self.master)
        self.entra_nome_anuncio.grid(pady=20,padx=20,column=1, row=1) 
        
        self.label_cliente = tk.Label(self.master)
        self.label_cliente.configure(text="Cliente",width=20,font=("bold", 10))
        self.label_cliente.grid(column=0, row=2) 
        self.entra_cliente = tk.Entry(self.master)
        self.entra_cliente.grid(pady=20,padx=20,column=1, row=2) 

        self.label_data_ini = tk.Label(self.master)
        self.label_data_ini.configure(text="Data de início",width=20,
                                      font=("bold", 10))
        self.label_data_ini.grid(column=0, row=3)
        self.entra_data_ini = tk.Entry(self.master)
        self.entra_data_ini.grid(pady=20,padx=20,column=1, row=3)
        self.calendario1 = tkcal.DateEntry(self.entra_data_ini)
        self.calendario1.configure(width=30,locale='pt_BR',background="blue",
                                   foreground="white")
        self.calendario1.grid()

        self.label_data_fim = tk.Label(self.master)
        self.label_data_fim.configure(text="Data de término",width=20,
                                      font=("bold", 10))
        self.label_data_fim.grid(column=0, row=4)
        self.entra_data_fim = tk.Entry(self.master)
        self.entra_data_fim.grid(pady=20,padx=20,column=1, row=4)
        self.calendario2 = tkcal.DateEntry(self.entra_data_fim)
        self.calendario2.configure(width=30,locale='pt_BR',background="blue",
                                   foreground="white")
        self.calendario2.grid()

        self.label_inv_dia = tk.Label(self.master)
        self.label_inv_dia.configure(text="Investimento Diário",width=20,
                                     font=("bold", 10))
        self.label_inv_dia.grid(column=0, row=5) 
        self.entra_inv_dia = tk.Entry(self.master)
        self.entra_inv_dia.grid(pady=20,padx=20,column=1, row=5) 

        # Botão para inserção/conferência dos dados digitados
        self.salvar_button = tk.Button(self.master)
        self.salvar_button.configure(text='Cadastrar', width=20,font=("bold", 10),
                                     command = self.combineFunc(self.func_01,
                                                      self.func_02,self.func_03,
                                                      self.func_04, self.func_05,
                                                      self.func_check))
                                                      
        self.salvar_button.grid(pady=20,padx=20,column=0, row=6)
        
        # Comando para sair da tela de cadastro
        # que chama a função específica para esse fim
        self.sair_cad_button = tk.Button(self.master)
        self.sair_cad_button.configure(text='Sair', width=20,font=("bold", 10),
                                     command = self.close_windows)
                                                      
        self.sair_cad_button.grid(pady=20,padx=20,column=1, row=6)        
   
    # função que chama as funções de captura e condicionamento individual dos
    # dados do cadastro
    def combineFunc(self, *funcs):
         def combinedFunc(*args, **kwargs):
             for f in funcs:
                 f(*args, **kwargs)
         return combinedFunc

    def func_01(self):
        global nome_anuncio
        nome_anuncio = self.entra_nome_anuncio.get()
        
        return

    def func_02(self):
        global cliente
        cliente = self.entra_cliente.get()
        
        return
        
    def func_03(self):
        global data_ini
        data = self.calendario1.get()
        # conversão da data do calendário para datetime.date
        data_ini = capt_data(data)
                
        return
        
    def func_04(self):
        global data_fim
        data = self.calendario2.get()
        # conversão da data do calendário para datetime.date
        data_fim = capt_data(data)
        
        return
       
    def func_05(self):
        global inv_dia
        inv = self.entra_inv_dia.get()
        # conversão da string 'valor investido' para float
        inv_dia = float(inv)
        
        return
        
    def func_check(self):
        # função que faz a conferência de dados ausentes/incompatíveis
        # chamando as funções de mensagem de erro se necessário
        global nome_anuncio, cliente, data_ini, data_fim, inv_dia
        dados = [nome_anuncio, cliente, data_ini, data_fim, inv_dia]
           
        if dados[0] == '':
            dado_ausente = 'Nome do Anúncio'
            self.mensagem_erro(dado_ausente)
            return False
    
        if dados[1] == '':
            dado_ausente = 'Cliente'
            self.mensagem_erro(dado_ausente)
            return False
        
        if dados[2] == '':
            dado_ausente = 'Data de início'
            self.mensagem_erro(dado_ausente)
            return False        
    
        if dados[3] == '':
            dado_ausente = 'Data de término'
            self.mensagem_erro(dado_ausente)
            return False  
        
        if dados[3] < dados[2]:
            self.mensagem_erro_datas(dados[2],dados[3])
            return False   
    
        if dados[4] == '':
            dado_ausente = 'Investimento Diário'
            self.mensagem_erro(dado_ausente)
            return False
        # não havendo erros no preenchimento:
        # - calcula o investimento total,
        # - adiciona esse valor a dados[]
        # - chama  a função para armazenar o registro no banco de dados
        n_dias =  (data_fim - data_ini).days + 1
        inv_total = n_dias * inv_dia
        dados.append(inv_total)
        armazena_dados(dados) 
        # Limpa os campos de dados que foram preenchidos
        self.limpa_dados()
        
        return

    def mensagem_erro(self,dado_ausente):
        # função que mostra mensagem de erro indicando o campo não preenchido
        texto = 'O campo: "' + dado_ausente + '" não foi preenchido.'
        self.msg_erro = tk.messagebox.showinfo('Dados incompletos!',texto,parent=self.master)
                
        return
    
    def mensagem_erro_datas(self,data_ini,data_fim):
        # função que mostra mensagem de erro indicando que as datas são
        # incompatíveis
        texto = 'A data de término: "' + str(data_fim) + '" é anterior à '
        texto = texto + 'data de início: "' + str(data_ini) + '.'            
        self.msg_erro = tk.messagebox.showinfo('Dados inconsistentes!',texto)    
        
        return

    def limpa_dados(self):
        # função que limpa os campos preenchido no cadastro
        self.entra_nome_anuncio.delete(0, 'end')
        self.entra_cliente.delete(0, 'end')
        self.calendario1.delete(0,'end')
        self.calendario2.delete(0,'end')
        self.entra_inv_dia.delete(0,'end')
        
        return

    def close_windows(self):
        # fecha a janela de cadastro
        self.master.destroy()

class Relatorio:
    # Classe da tela de relatório
    # As variáveis que compõem os dados do relatório são globais nesta classe
    global cliente_rel, interv_ini, interv_fim
    # Criação dos widgets da tela de cadastro
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.attributes('-topmost', True)
        self.label_titulo = tk.Label(self.master)
        self.label_titulo.configure(text="Solicitar Relatório de Anúncios",width=30,
                                    font=("bold", 20))
        self.label_titulo.grid(column=0, row=0) 
        self.label_cliente_rel = tk.Label(self.master)
        self.label_cliente_rel.configure(text="Cliente",width=20,font=("bold", 10))
        self.label_cliente_rel.grid(column=0, row=1) 
        self.entra_cliente_rel = tk.Entry(self.master)
        self.entra_cliente_rel.grid(pady=20,padx=20,column=1, row=1) 

        self.label_interv_ini = tk.Label(self.master)
        self.label_interv_ini.configure(text="Data de início do intervalo de pesquisa",width=40,
                                      font=("bold", 10))
        self.label_interv_ini.grid(column=0, row=2)
        self.entra_interv_ini = tk.Entry(self.master)
        self.entra_interv_ini.grid(pady=20,padx=20,column=1, row=2)
        self.calendario_a = tkcal.DateEntry(self.entra_interv_ini)
        self.calendario_a.configure(width=30,locale='pt_BR',background="blue",
                                   foreground="white")
        self.calendario_a.grid()

        self.label_interv_fim = tk.Label(self.master)
        self.label_interv_fim.configure(text="Data de término do intervalo de pesquisa",width=40,
                                      font=("bold", 10))
        self.label_interv_fim.grid(column=0, row=3)
        self.entra_interv_fim = tk.Entry(self.master)
        self.entra_interv_fim.grid(pady=20,padx=20,column=1, row=3)
        self.calendario_b = tkcal.DateEntry(self.entra_interv_fim)
        self.calendario_b.configure(width=30,locale='pt_BR',background="blue",
                                   foreground="white")
        self.calendario_b.grid()

        # Comando para inserção/conferência dos dados digitados
        self.gerar_button = tk.Button(self.master)
        self.gerar_button.configure(text='Gerar Relatório', width=20,font=("bold", 10),
                                     command = self.combineFunc(self.func_01,
                                                      self.func_02,self.func_03,
                                                      self.func_check))
                                                      
        self.gerar_button.grid(pady=20,padx=20,column=0, row=6)
        
        # Comando para sair da tela de relatório
        self.sair_cad_button = tk.Button(self.master)
        self.sair_cad_button.configure(text='Sair', width=20,font=("bold", 10),
                                     command = self.close_windows)
                                                      
        self.sair_cad_button.grid(pady=20,padx=20,column=1, row=6)    

    def combineFunc(self, *funcs):
         def combinedFunc(*args, **kwargs):
             for f in funcs:
                 f(*args, **kwargs)
         return combinedFunc
 
    def func_01(self):
        global cliente_rel
        cliente_rel = self.entra_cliente_rel.get()
        
        return
        
    def func_02(self):
        global interv_ini
        data = self.calendario_a.get()
        # conversão da data do calendário para datetime.date
        interv_ini = capt_data(data)
                
        return
        
    def func_03(self):
        global interv_fim
        data = self.calendario_b.get()
        # conversão da data do calendário para datetime.date
        interv_fim = capt_data(data)
 
    def func_check(self):
        global cliente_rel, interv_ini, interv_fim
        dados = [cliente_rel,interv_ini, interv_fim]
    
        if dados[0] == '':
            dado_ausente = 'Cliente'
            self.mensagem_erro(dado_ausente)
            
            return
        
        if dados[1] == '':
            dado_ausente = 'Data de início do intervalo'
            self.mensagem_erro(dado_ausente)
            return False        
    
        if dados[2] == '':
            dado_ausente = 'Data de término do intervalo'
            self.mensagem_erro(dado_ausente)
            return False      

        if dados[2] < dados[1]:
            self.mensagem_erro_datas(dados[1],dados[2])
            return False   

        # não havendo erros no preenchimento:
        # - chama  a função para extrair o relatório da base de dados
        extrai_relatorio(dados)
        # Limpa os campos de dados que foram preenchidos
        self.limpa_dados()
 
        return 

    def mensagem_erro(self,dado_ausente):
        # função que mostra mensagem de erro indicando o campo não preenchido
        texto = 'O campo: "' + dado_ausente + '" não foi preenchido.'
        self.msg_erro = tk.messagebox.showinfo('Dados incompletos!',texto,parent=self.master)
                
        return

    def mensagem_erro_datas(self,data_ini,data_fim):
        # função que mostra mensagem de erro indicando que as datas são
        # incompatíveis
        texto = 'A data de término: "' + str(data_fim) + '" é anterior à '
        texto = texto + 'data de início: "' + str(data_ini) + '.'            
        self.msg_erro = tk.messagebox.showinfo('Dados inconsistentes!',texto)    
        
        return

    def limpa_dados(self):
        # função que limpa os campos preenchido no cadastro
        self.entra_cliente_rel.delete(0, 'end')
        self.entra_interv_ini.delete(0,'end')
        self.entra_interv_fim.delete(0,'end')       
        
        return
        
    def close_windows(self):
        self.master.destroy()

## 2. Definição das funções de manipulação de dados e de interação com
## a  base de dados

def capt_data(data):
    #recebe uma string no formato data dd/mm/aaa e devolve como datetime.date
    data_var = datetime.date(int(data[6:10]),int(data[3:5]),int(data[0:2]))
    return data_var

def check_db(config):
    # Confere a conexão e cria a a base de dados e a 
    # tabela  caso não existam de acordo com os valores
    # da lista de parâmetros 'config'
    
    # a. Conexão com o Banco de Dados Mysql
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  )
    if conector:
        print('Conectado ao Banco de Dados')
        print(conector)
    else:
        print("Não foi possível conectar com o banco de dados")
     
    # b. Definição do cursor para a base de dados
    cursor = conector.cursor()

    # c. Verifica/cria a base de dados e fecha a conexão
    query = "CREATE DATABASE IF NOT EXISTS " + config[3] 
    cursor.execute(query)
    conector.close()
    
    # d. Reconecta com o servidor utilizando a base de dados especificada
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  database=config[3]
                                  )    
    cursor = conector.cursor()
    # e. Verifica/cria a Tabela e fecha a conexão
    query ="CREATE TABLE IF NOT EXISTS " + config[4] + """
       (nome CHAR(70) NOT NULL,
       cliente CHAR(50) NOT NULL,
       data_ini DATE NOT NULL,
       data_fim DATE NOT NULL,
       investimento_diario FLOAT,
       inv_total FLOAT,
       n_max_visualizacoes INT,
       n_max_cliks INT,
       n_max_compartilhamentos INT
    )"""
    cursor.execute(query)
    conector.close()

def armazena_dados(dados):
    # função primária para armazenar o registro completo do anúncio na base de
    # dados
    # utiliza a variável global 'db_config'
    global db_config

    # a. Chama a função 'calcula_reperc' que irá retornar as quantidades 
    # máximas de visualizações, cliks e compartilhamentos com base no 
    # investimento total
    inv_total = dados[5]
    reperc = calcula_repercussao(inv_total)
    
    # b. acrescenta esses valores à lsita 'dados'
    dados = dados + reperc
    
    # c. com os dados completos chama a função que se conecta à base de dados e
    # insere o registro
    if anuncio_to_table(db_config,dados):
        return True

    else:
        return False

def anuncio_to_table(config,registro):
    # função que se conecta à base de dados e insere o registro
    
    # a. Conexão com o Banco de Dados Mysql
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  database=config[3])
  
    # b. definição do cursor para a base e execução da query que insere os
    # dados do registro compelto na tabela, definida por 'config[4]'
    cursor = conector.cursor()
    query= "INSERT INTO " + config[4] + """
    (nome, cliente, data_ini,data_fim,investimento_diario,inv_total,
    n_max_visualizacoes,n_max_cliks, n_max_compartilhamentos) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    val = (registro[0],registro[1],registro[2],registro[3],registro[4],
           registro[5],registro[6],registro[7],registro[8])
    cursor.execute(query, val)
    conector.commit()

    print(cursor.rowcount, 'registros inseridos')    

    # fecha a conexão com a base de dados
    conector.close()
    
    return True

def extrai_relatorio(dados):
    # função primária para gerar o relatório com base no cliente e no intervalo
    # de dias do anúncio.
    # Recebe a lista 'dados' e chama a função para realizar a transação com o
    # de dados fornecendo os parâmetros contidos na variável global db_config
    global db_config
    relatorio_from_table(db_config,dados)
    
    return

def relatorio_from_table(config,parametros):
    # função para gerar o relatório da base de dados
    # a. Conexão com o Banco de Dados Mysql
    # A lista parâmetros contém o cliente, data de início e data de término
    # do intervalo considerado para o relatório, nessa ordem.
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  database=config[3])
  
    # b. Query que especifica o cliente e as datas do intervalo considerado
    # para o relatório
    query = "SELECT * FROM " + config[4] + """
            WHERE cliente = %s 
            AND data_ini >= %s
            AND data_fim <= %s
            
            ORDER BY nome
            """
    # c. Importação direta do resultado da query para um dataframe Pandas
    df = pd.read_sql(sql=query,params=[parametros[0],parametros[1],
                                       parametros[2]],con=conector)
   
    # d. Ordenação e escolha dos campos para o relatório
    df_rel = df[['cliente','nome','inv_total','n_max_visualizacoes',
                 'n_max_cliks','n_max_compartilhamentos']]
    
    # e. Visualização do relatório através de arquivo html/browser
    rel_browser(df_rel)
    conector.close()
    return 

def rel_browser(df):
    # função que recebe um dataframe e gera viusalização desse dataframe
    # em forma de tabela no browser
    with NamedTemporaryFile(mode ='w',delete=False, suffix='.html') as f:
        df.to_html(f)
    webbrowser.open(f.name)    


def calcula_repercussao(inv_total):
    # Chama o módulo da calculadora com o investimento total como parâmetro
    # o qual retorna o resultado com os três dados de repercussão na lista
    # 'reperc': número máximo de visualizações, de cliks e de compartilhamentos,
    # nessa ordem

    reperc = calc.main(inv_total)
     
    return reperc

def main():
    global db_config
    db_config = ['username','password','host','database_name','table_name']
    check_db(db_config)
    root = tk.Tk()
    Principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()
  