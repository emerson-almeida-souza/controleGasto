import BANCO.banco as bd
from FONTES.menus import *
from FONTES.menuCategoriaGasto import menuCategoriaGasto
import pandas as pd
import PySimpleGUI as sg

sg.theme('DARKGREY4')
#CONSTANTES
defaultSizeButton = 30
defaultSizeText = 11
defaultTheme = 'Georgia'
defaultColorButton = '#469536'
defaultColorWindow = '#dbead5'

#LIST MENUS
categorias = ["BANCOS", "DOMÉSTICO"]
diaVencimento = [5, 15]
pago = ['NÃO', 'SIM']

DADOS = bd.buscaTudo() 
headers = list(DADOS)

dadosGasto = [] #ARMAZENA TODOS OS DADOS
Nlinha, Ncoluna = DADOS.shape

def upperData(headers):
    headerUP = []
    for head in headers:
        headerUP.append(str(head).upper())
    
    return headerUP

def listarGastos():
    dadosGasto = []
    for linha in range(Nlinha):  #NAVEGA LINHA POR LINHA
        data = [] #CRIA A LISTA DA LINHA
        for coluna in range(Ncoluna):
            data.append(DADOS[headers[coluna]][linha]) #ADICIONA CADA DADO DA LINHA NA LISTA

        dadosGasto.append(data) #ADICIONA VÁRIAS LINHAS NA LIST

    print(dadosGasto) 
    return dadosGasto

#TELAS
def telaInicial():
    layout = [
    [sg.Button('CADASTRAR GASTO', key='-CD-', size=defaultSizeButton, button_color=defaultColorButton, font=(defaultTheme, defaultSizeText, 'bold', 'underline'))],#ALTERAR COR
    [sg.Button('EXIBIR TODOS OS GASTOS', key='-TG-', size=defaultSizeButton, button_color=defaultColorButton, font=(defaultTheme, defaultSizeText, 'bold', 'underline'))] #CONFIGURAR DEFAULT SIZEBUTTON
    
]
    return sg.Window('CONTROLE DE GASTOS', layout=layout, element_justification='c', finalize=True) #modal = true, tem que fechar essa janela pras outras funcionarem

def exibirDados(TOTAL_GASTO, SALDO_FINAL, dadosGasto):
    
    headersUpper = upperData(headers)
    
    layout = [ 
    [
        sg.Table(values=dadosGasto,
                 headings=headersUpper,
                 max_col_width=100,
                 background_color='lightblue',
                 justification='center',
                 alternating_row_color='lightyellow',
                 key='-TABELA-',
                 text_color='BLACK',
                 header_font=("Helvetica", 10, 'bold')
                #  bind_return_key=True, #DOUBLE CLICK
                #  selected_row_colors=('RED', 'GREEN'),
                #  expand_x = True,
                #  expand_y = True
                #  right_click_menu = ['&Right', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']] 
                 )
    ],
    
    [sg.Text('TOTAL GASTO:', font=('VERDANA', 14, 'bold')) ,sg.Text(f'R$ {TOTAL_GASTO}', key='-TGASTO-', text_color='#00995D', font=('VERDANA', 15, 'bold', 'underline')), sg.Push()],
    [sg.Text('SOBRAS PÓS GASTO:', font=('VERDANA', 14, 'bold')),sg.Text(f'R$ {SALDO_FINAL}', key='-SOBRAS-', text_color='#900020', font=('VERDANA', 15, 'bold', 'underline')), sg.Push()]
]
    return sg.Window('CONTROLE DE GASTOS', layout=layout, element_justification='c', element_padding=(25, 1), finalize=True) #Distancia entre os elementos

def cadastraGasto():
    cadastro = [
    [sg.Text('NOME DO CUSTO')],
    [sg.Input(key='-NGASTO-')],
    [sg.HSep()],
    
    [sg.Text('VALOR')],
    [sg.Input(key='-VALOR-', )],
    [sg.HSep()],
    
    [sg.Text('CATEGORIA')],
    [sg.Combo(values=categorias, default_value= categorias[0], enable_events=True, readonly=True, k='-CATEGORIA-', size=(15,15))],
    [sg.HSep()],#linha separadora
    
    [sg.Text('DIA DO VENCIMENTO')],
    [sg.Combo(values=diaVencimento, default_value= diaVencimento[0], enable_events=True, readonly=True, k='-VENCIMENTO-', size=(15,15))],
    [sg.HSep()],#linha separadora
    
    [sg.Text('O GASTO FOI PAGO ?')],
    [sg.Combo(values=pago, default_value= pago[0], enable_events=True, readonly=True, k='-PAGO-', size=(15,15))],
    [sg.HSep()],
    
    [sg.Push(),sg.Button('CADASTRAR', key='-CADASTRAR-', size=defaultSizeButton, button_color=defaultColorButton, font=(defaultTheme, defaultSizeText, 'bold', 'underline')), sg.Push()],
    [sg.Push(), sg.Text('DEFAULT', key='-MENSAGEM-'), sg.Push()] #centralizar um elemento
]
    
    layout = [[sg.Frame('CADASTRO', layout=cadastro)]
]
    return sg.Window('CONTROLE DE GASTOS', layout=layout, finalize=True)

janela1, janela2 = telaInicial(), None

while True:
    window, event, values = sg.read_all_windows()
 
    print(window, event, values)
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    
    if window == janela2 and  event == sg.WIN_CLOSED:
        janela2.close()
        janela1.un_hide()
        
    
    if window == janela1 and event == '-CD-':
        janela2 = cadastraGasto()
        janela2.force_focus()
        janela1.hide()

    if window == janela1 and event == '-TG-':
        dadosGasto = listarGastos()
        TOTAL_GASTO = float(DADOS['valor'].sum())
        SALDO = 1148
        SALDO_FINAL = SALDO - TOTAL_GASTO 
        
        janela2 = exibirDados(TOTAL_GASTO, SALDO_FINAL, dadosGasto)
        janela2.force_focus()
        janela1.hide()

    if window == janela2 and event == '-CADASTRAR-':
        try:
            nGasto = str(values['-NGASTO-'])
            valor = float(values['-VALOR-'])
            categoria = str(values['-CATEGORIA-'])
            vencimento = str(values['-VENCIMENTO-'])
            pago = str(values['-PAGO-'])
            bd.inserirTabela(nome=nGasto, valor=valor, categoria=categoria, vencimentoDia=vencimento, pago=0)
            window['-MENSAGEM-'].update('DADO CADASTRADO COM SUCESSO!')
        except Exception as erro:
            window['-MENSAGEM-'].update('ERRO AO CADASTRAR!')
        
    if window == janela2 and event == '-TABELA-':
        pass
        # if values['-TABELA-'] == [0]:
        #     janela2 = cadastraGasto()
    
