# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:40:46 2021

@author: augusto.pavao
"""

import tkinter as tk

import tkinter.messagebox

import tkcalendar as tkcal

import pandas as pd

import datetime

import mysql.connector 

import calculadora as calc

class Principal:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, width = 1400, height = 300)
        self.titulo = tk.Label(self.frame, text="Sistema de Cadastro de Anúncios",
                               font=('Arial', 25))
        self.titulo.pack(padx=100,pady=50)

        self.button1 = tk.Button(self.frame, text = 'Cadastrar novo Anúncio',
                                 width = 100, font=('Arial', 15),bg='#0059b3',
                                 command = self.w_cadastro)
        self.button1.pack(padx=100,pady=50)

        self.button2 = tk.Button(self.frame, text = 'Gerar Relatório',
                                 width = 100, font=('Arial', 15),
                                 command = self.w_relatorio)
        self.button2.pack(padx=100,pady=50)        
        self.frame.pack()

        self.button3 = tk.Button(self.frame, text = 'Sair do Sistema',
                                 width = 100, font=('Arial', 15),
                                 command = self.close_windows)
        self.button3.pack(padx=100,pady=50)        
        self.frame.pack()

    def w_cadastro(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Cadastro(self.newWindow)
            
    def w_relatorio(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Relatorio(self.newWindow)

    def close_windows(self):
        self.master.destroy()

class Cadastro:
    global nome_anuncio, cliente, data_ini, data_fim, inv_dia
    nome_anuncio, cliente, data_ini, data_fim, inv_dia = '','','','',''
    
    def __init__(self, master):
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
        self.label_data_ini.configure(text="Data de início",width=20,font=("bold", 10))
        self.label_data_ini.grid(column=0, row=3)
        self.entra_data_ini = tk.Entry(self.master)
        self.entra_data_ini.grid(pady=20,padx=20,column=1, row=3)
        self.calendario1 = tkcal.DateEntry(self.entra_data_ini)
        self.calendario1.configure(width=30,locale='pt_BR',background="blue",foreground="white")
        self.calendario1.grid()

        self.label_data_fim = tk.Label(self.master)
        self.label_data_fim.configure(text="Data de término",width=20,font=("bold", 10))
        self.label_data_fim.grid(column=0, row=4)
        self.entra_data_fim = tk.Entry(self.master)
        self.entra_data_fim.grid(pady=20,padx=20,column=1, row=4)
        self.calendario2 = tkcal.DateEntry(self.entra_data_fim)
        self.calendario2.configure(width=30,locale='pt_BR',background="blue",foreground="white")
        self.calendario2.grid()

        self.label_inv_dia = tk.Label(self.master)
        self.label_inv_dia.configure(text="Investimento Diário",width=20,font=("bold", 10))
        self.label_inv_dia.grid(column=0, row=5) 
        self.entra_inv_dia = tk.Entry(self.master)
        self.entra_inv_dia.grid(pady=20,padx=20,column=1, row=5) 

        # Comando para inserção/conferência dos dados digitados
        self.salvar_button = tk.Button(self.master)
        self.salvar_button.configure(text='Cadastrar', width=20,font=("bold", 10),
                                     command = self.combineFunc(self.func_01,
                                                      self.func_02,self.func_03,
                                                      self.func_04, self.func_05,
                                                      self.func_check))
                                                      
        self.salvar_button.grid(pady=20,padx=20,column=0, row=6)
        
        # Comando para sair da tela de cadastro
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
           global nome_anuncio
           nome_anuncio = self.entra_nome_anuncio.get()
           print(nome_anuncio)

    def func_02(self):
        global cliente
        cliente = self.entra_cliente.get()
        
    def func_03(self):
        global data_ini
        data = self.calendario1.get()
        data_ini = capt_data(data)
        print(data_ini)
        
    def func_04(self):
        global data_fim
        data = self.calendario2.get()
        data_fim = capt_data(data)
        print(data_fim)

    def func_05(self):
        global inv_dia
        inv = self.entra_inv_dia.get()
        inv_dia = float(inv)
        
        
    def func_check(self):
        #dados = self.get_dados(self)
        global nome_anuncio, cliente, data_ini, data_fim, inv_dia
        dados = [nome_anuncio, cliente, data_ini, data_fim, inv_dia]
        print(dados)
    
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
        # não havendo erros no preenchimento, calcula o investimento total,
        # adiciona a dados[] e chama  a função para
        # armazenar o registro no data frame
        #date1 = datetime.datetime.strptime(data_ini, "%Y-%m-%d").date()
        #date2 = datetime.datetime.strptime(data_fim, "%Y-%m-%d").date()
        n_dias =  (data_fim - data_ini).days + 1
        print('número de dias encontrado: ',n_dias)
        inv_total = n_dias * inv_dia
        dados.append(inv_total)
        armazena_dados(dados) # chama função que transfere os dados do cadastro salvo para
        # a base de dados
        # Limpa os campos de dados que foram perenchidos
        self.limpa_dados()
        return True # se todos os dados foram preenchidos corretamente
                    # a função retorna 'True'

    def mensagem_erro(self,dado_ausente):
        texto = 'O campo: "' + dado_ausente + '" não foi preenchido.'
        self.msg_erro = tk.messagebox.showinfo('Dados incompletos!',texto,parent=self.master)
                
        return
    
    def mensagem_erro_datas(self,data_ini,data_fim):
        texto = 'A data de término: "' + str(data_fim) + '" é anterior à '
        texto = texto + 'data de início: "' + str(data_ini) + '.'            
        self.msg_erro = tk.messagebox.showinfo('Dados incompletos!',texto)    
        
        return

    def limpa_dados(self):
        self.entra_nome_anuncio.delete(0, 'end')
        self.entra_cliente.delete(0, 'end')
        self.calendario1.delete(0,'end')
        self.calendario2.delete(0,'end')
        self.entra_inv_dia.delete(0,'end')
        
        return

    def close_windows(self):
        self.master.destroy()

class Relatorio:
    global cliente_rel, periodo
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.attributes('-topmost', True)
        self.label_titulo = tk.Label(self.master)
        self.label_titulo.configure(text="Solicitar Relatório de Anúncios",width=20,
                                    font=("bold", 20))
        self.label_titulo.grid(column=0, row=0) 
        self.label_cliente_rel = tk.Label(self.master)
        self.label_cliente_rel.configure(text="Cliente",width=20,font=("bold", 10))
        self.label_cliente_rel.grid(column=0, row=1) 
        self.entra_cliente_rel = tk.Entry(self.master)
        self.entra_cliente_rel.grid(pady=20,padx=20,column=1, row=1) 

        self.label_titulo.grid(column=0, row=0) 
        self.label_periodo = tk.Label(self.master)
        self.label_periodo.configure(text="Dias agendados",width=20,font=("bold", 10))
        self.label_periodo.grid(column=0, row=2) 
        self.entra_periodo = tk.Entry(self.master)
        self.entra_periodo.grid(pady=20,padx=20,column=1, row=2) 

        # Comando para inserção/conferência dos dados digitados
        self.gerar_button = tk.Button(self.master)
        self.gerar_button.configure(text='Gerar Relatório', width=20,font=("bold", 10),
                                     command = self.combineFunc(self.func_01,
                                                      self.func_02, self.func_check))
                                                      
        self.gerar_button.grid(pady=20,padx=20,column=0, row=6)
        
        # Comando para sair da tela de relatório
        self.sair_cad_button = tk.Button(self.master)
        self.sair_cad_button.configure(text='Sair', width=20,font=("bold", 10),
                                     command = self.close_windows)
                                                      
        self.sair_cad_button.grid(pady=20,padx=20,column=1, row=6)    

####
    def combineFunc(self, *funcs):
         def combinedFunc(*args, **kwargs):
             for f in funcs:
                 f(*args, **kwargs)
         return combinedFunc
 
    def func_01(self):
        global cliente_rel
        cliente_rel = self.entra_cliente_rel.get()
        
    def func_02(self):
        global periodo
        dias = self.entra_periodo.get()
        periodo = int(dias)
 
    def func_check(self):
        global cliente_rel, periodo
        dados = [cliente_rel, periodo]
        print(dados)
    
        if dados[0] == '':
            dado_ausente = 'Cliente'
            self.mensagem_erro(dado_ausente)
            return False
        
        if dados[1] == '':
            dado_ausente = 'Dias Agendados'
            self.mensagem_erro(dado_ausente)
            return False        
 

        # não havendo erros no preenchimento, chama  a função para
        # extrair o relatório da base de dados
        extrai_relatorio(dados)
        # Limpa os campos de dados que foram preenchidos
        self.limpa_dados()
        return True # se todos os dados foram preenchidos corretamente
                    # a função retorna 'True'

    def mensagem_erro(self,dado_ausente):
        texto = 'O campo: "' + dado_ausente + '" não foi preenchido.'
        self.msg_erro = tk.messagebox.showinfo('Dados incompletos!',texto,parent=self.master)
                
        return

    def limpa_dados(self):
        self.entra_cliente_rel.delete(0, 'end')
        self.entra_periodo.delete(0,'end')
       
        
        return

####
        
    def close_windows(self):
        self.master.destroy()

# Funções 

def capt_data(data):
    #recebe uma string no formato data dd/mm/aaa e devolve variável data do python
    data_var = datetime.date(int(data[6:10]),int(data[3:5]),int(data[0:2]))
    return data_var

def check_db(config):
    # Confere a conexão e cria a a base de dados 'anuncios_db' e a 
    # Tabela 'anuncios' caso não existam
    # 1. Conexão com o Banco de Dados Mysql
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  )
    if conector:
        print('Conectado ao Banco de Dados')
        print(conector)
    else:
        print("Não foi possível conectar com o banco de dados")
     
    # 2. Definição do cursor para a base de dados
    cursor = conector.cursor()

    # 3. Verifica/cria a base de dados
    query = "CREATE DATABASE IF NOT EXISTS " + config[3] 
    cursor.execute(query)
    
    # 4. Reconecta com o servidor utilizando a base de dados
    conector.close()
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  database=config[3]
                                  )    
    cursor = conector.cursor()
    # 4. Verifica/cria a Tabela
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

def anuncio_to_table(config,registro):
    # Conexão com o Banco de Dados Mysql
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  database=config[3])
  
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

    conector.close()

def relatorio_from_table(config,parametros):
    print('parametros: ',parametros)
    # Conexão com o Banco de Dados Mysql
    conector = mysql.connector.connect(user=config[0],
                                  password=config[1],
                                  host=config[2],
                                  database=config[3])
  
    cursor = conector.cursor()
    query = "SELECT * FROM " + config[4] + """
            WHERE cliente = %s 
            AND inv_total/investimento_diario = %s
            
            ORDER BY nome
            """
            
    val = (parametros[0],)
    #cursor.execute(query,val)
    df_rel = pd.read_sql(sql=query,params=[parametros[0],parametros[1]],
                         con=conector)
    print(df_rel)
    conector.close()
    return 

# O sistema fornecerá os relatórios de cada anúncio contendo:
# valor total investido
#quantidade máxima de visualizações
#quantidade máxima de cliques
#quantidade máxima de compartilhamentos
#Os relatórios poderão ser filtrados por intervalo de tempo e cliente.


def armazena_dados(dados):
    global db_config
    print('dados_fora da classe formulario: ',dados)
    inv_total = dados[5]
    reperc = calcula_repercussao(inv_total)
    dados = dados + reperc
    print('dados completos: ', dados)
    anuncio_to_table(db_config,dados)

    return

def extrai_relatorio(dados):
    global db_config
    relatorio_from_table(db_config,dados)
    
    return

def calcula_repercussao(inv_total):
    # Chama o módulo da calculadora com o investimento total
    # e retorna o resultado com os três parâmetros de repercussão

    reperc = calc.main(inv_total)
    print('resultado da calculadora: ',reperc)
    
    return reperc

def main():
    global db_config
    db_config = ['augusto','astra#2018','127.0.0.1','anuncios_db','tab_anuncios']
    check_db(db_config)
    root = tk.Tk()
    app = Principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
    
"""
def call():
    res = mb.askquestion('Exit Application', 
                         'Do you really want to exit')
      
    if res == 'yes' :
        root.destroy()
          
    else :
        mb.showinfo('Return', 'Returning to main application')
  
# Driver's code
root = tk.Tk()
canvas = tk.Canvas(root, 
                   width = 200, 
                   height = 200)
  
canvas.pack()
b = Button(root,
           text ='Quit Application',
           command = call)
  
canvas.create_window(100, 100, 
                     window = b)
  
root.mainloop()


##########

import tkinter
from tkinter import messagebox
 
messagebox.askokcancel("Title","The application will be closed")
messagebox.askyesno("Title","Do you want to save?")
messagebox.askretrycancel("Title","Installation failed, try again?")
"""