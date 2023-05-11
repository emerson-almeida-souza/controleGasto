import sqlite3
import pandas as pd 
import datetime as dt

PATH = 'BANCO/Gastos.db'
conexao = sqlite3.connect(PATH)
cursor = conexao.cursor()

#MELHORAR DIAVENCIMENTO
def createFirstTable():
    DATA_ATUAL = dt.date.today()
    cursor.execute(
    f"""CREATE TABLE Gasto(
    nome VARCHAR NOT NULL, 
    valor DOUBLE NOT NULL,
    diaVencimento VARCHAR NOT NULL,
    pago INT NOT NULL
    )
    """
    )

def create(nome, valor, diaVencimento, pago):
    cursor.execute(f"INSERT INTO Gasto (nome, valor, diaVencimento, pago) VALUES (?, ?, ?, ?)", (nome, valor, diaVencimento, pago, ))
    conexao.commit() 

def readAll():
    data = cursor.execute('SELECT rowid, nome, valor, diaVencimento, pago FROM Gasto').fetchall()
    return data

def readOne(id):
    data = cursor.execute('SELECT rowid, nome, valor, diaVencimento, pago FROM Gasto WHERE rowid = ?', (id, )).fetchone()
    return data

def update(id ,nome, valor, diaVencimento):
    #CAMPO ESPECIFICO
    #CRIAR FUNÇÕES ESPECIFICAS
    atualizaNome = f"UPDATE Gasto set nome = {nome}, valor = {valor}, diaVencimento = {diaVencimento} WHERE rowid = ?", (id, )
    atualizaValor = f"UPDATE Gasto set nome = {nome}, valor = {valor}, diaVencimento = {diaVencimento} WHERE rowid = ?", (id, )
    atualizaDiaVencimento = f"UPDATE Gasto set nome = {nome}, valor = {valor}, diaVencimento = {diaVencimento} WHERE rowid = ?", (id, )

    #OU TUDO
    queryAtualizaTudo = f"UPDATE Gasto set nome = {nome}, valor = {valor}, diaVencimento = {diaVencimento} WHERE rowid = ?", (id, )
    cursor.execute(queryAtualizaTudo)
    conexao.commit() 

def delete(id):
    cursor.execute(f"DELETE Gasto WHERE rowid = ?", (id, ))

def setPago(id):
    cursor.execute(f"UPDATE Gasto set pago = 1 WHERE rowid = ?", (id, ))
    conexao.commit() 

createFirstTable()