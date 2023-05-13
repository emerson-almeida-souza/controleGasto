import os
import BANCO.banco as bd
from CLASSES.Gasto import Gasto
import calendar
import datetime

def validaNome():
    os.system("cls")
    validado = False

    while validado == False:
        nome = input('Nome: ')
        
        if nome == "":
            print("O nome não pode ser vázio!")
            pressioneParaContinuar()
        else:
            validado = True

    return nome

def validaValor():
    os.system("cls")
    valor = None

    while True:
        try:
            valor = float(input("Digite um valor: "))
            if valor <= 0:
              raise ValueError("Valor inválido! O valor não pode ser menor que zero")
            break
        except ValueError as ve:
            if "could not convert" in str(ve):
                print("Valor inválido! Digite um valor em formato de moeda EX: R$1.00")
                pressioneParaContinuar()
            else:
                print(ve)
                pressioneParaContinuar()
    
    return valor

def validaData():
    os.system("cls")
    diaVencimento = None
    mesVencimento = None
    anoVencimento = None
    #Parametros para função monthrange()
    # indiceQuantosDiasMesdiaDaSemana = 0 
    indiceQuantosDiasMes = 1
    quantidadeDiasMes = None
    anoAtual = datetime.date.today().year
    data = None
    
    while True:
        try:
            diaVencimento = int(input("Digite o dia de vencimento do gasto: "))
            mesVencimento = int(input("Digite o mês de vencimento do gasto: "))
            anoVencimento = int(input("Digite o ano de vencimento do gasto: "))
            
            quantidadeDiasMes = calendar.monthrange(anoVencimento, mesVencimento)[indiceQuantosDiasMes] #Armazena quantos dias tem no mês digitado.

            if diaVencimento >= quantidadeDiasMes or diaVencimento < 1:
                raise ValueError("Dia inválido para o mês fornecido!")
                
            if anoVencimento < anoAtual:
                raise ValueError('O ano do gasto precisa ser o ano atual ou os próximos anos!')

            break
        except ValueError as ve:
            if "could not convert" in str(ve):
                print("Valor inválido. Digite uma data com nÚmeros inteiros!")
                pressioneParaContinuar()
            else:
                print(ve)
                pressioneParaContinuar()
    
    data = f'{diaVencimento}/{mesVencimento}/{anoVencimento}'
    return data

#continuar
def validaId():
    os.system("cls")
    id = None
    while True:
        try:
            id = int(input("Digite um valor: "))
            if len(gasto) == 0:
                raise ValueError("O ID não existe na base dados, por favor insira um valor válido!")
            if id <= 0:
              raise ValueError("Valor inválido! O ID não pode ser negativo!")
            break
        except ValueError as ve:
            if "could not convert" in str(ve):
                print("Valor inválido! Digite um valor em formato de moeda EX: R$1.00")
                pressioneParaContinuar()
            else:
                print(ve)
                pressioneParaContinuar()
    
    return valor

def registrarContaPaga():
    pass

def inserirFinanciamento():
    pass

def inputs(): 
    nome = validaNome()
    valor = validaValor()
    diaVencimento = validaData()
    pago = 0
    gasto = Gasto(nome, valor, diaVencimento, pago)
    return gasto

def createGasto(gasto: Gasto):
    bd.create(gasto.nome, gasto.valor, gasto.diaVencimento, gasto.pago)

def readGastos():
    gastos = bd.readAll()
    return gastos

def readGasto():
    id = validaId()

def updateGasto(id, nome, valor, categoria, diaVencimento):
    bd.update(id,nome, valor, categoria, diaVencimento)

def updateCampoEspecifico(campo, valor):
    pass

def updatePago(id):
    gasto = bd.readOne(id) 
    mensagem = None
    idValidade = validaId(id)
        
    
def deletarGasto(id):
    bd.delete(id)

def gerar_excel(DADOS, descricao):
    pass

def pressioneParaContinuar():
    input("Pressione qualquer tecla para continuar... ")
    os.system("cls")

def menuPrincipal():
    menus = [
         "\b[1 - INSERIR UM GASTO]",
         "\b[2 - EXIBIR MEUS GASTOS]",
         "\b[3 - ATUALIZAR UM GASTO]",
         "\b[4 - EXCLUIR REGISTRO]",
         "\b[5 - SALVAR EM UM ARQUIVO EXCEL",
         "\b[6 - SAIR]"]
    
    print(menus)

class cores:
    reset_color = "\033[0m"
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    blue = "\033[1;34;40m"
    magenta = "\033[1;35;40m"
    cyan = "\033[1;36;40m"

def calculoSaldo(saldo):
    pass