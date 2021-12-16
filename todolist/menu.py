from mysql.connector.dbapi import STRING
from principal import List, criarBase, criarTabela
from datetime import date, datetime, time
import os

print('+-'*20, 'To-do List', '+-'*20)

#Variável que executa as funções para criação do banco de dados e da tabela, respectivamente.
criacao = criarBase(), criarTabela()

#Instancia o Objeto.
tarefa1 = List()

#while True permite execução do trecho repetidamente até que encontre o elemento break.
while True:
    
    #Variável OPC obtém o que o usuário digitar e com base nisso a sequência de if/elif/else/ é executada.
    opc = input('Selecione o que deseja fazer no software:\nA-Salvar nova tarefa\nB-Visualizar tarefas salvas\nC-Deletar tarefa\nD-Sair do programa\n').upper()

    if opc == 'A':
        detalhes = input('Informe os detalhes da tarefa que pretende realizar:\n')
        dia = input('Informe a data:\n')
        hora = input('Informe o horário:\n')
        local = input('Informe o local:\n')
        if detalhes == dia == hora == local == "":
            print('Você precisa informar os valores!')
            break
        else:
            tarefa1.coleta_dados(detalhes,dia,hora,local)
        
    elif opc == 'B':
        tarefa1.Verificar()

    elif opc == 'C':
        val = int(input('Digite o id da tarefa que deseja remover:\n'))
        tarefa1.Deletar(val)
    
    elif opc == 'D':
        print('Fim do programa')
        break
    else:
        print('Comando Inválido, tente novamente!')
        
    
