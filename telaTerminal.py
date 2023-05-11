from FONTES.funcoes import *
import os

def main():
    
    while True:     
        menuPrincipal()
        op = input("..: ")
        os.system("cls")
        match op:
            case '1':
                inserirGasto()
                
            case '2':
                exibirGastos()   
                
            case '3':
                atualizarGasto()
                
            case '4':
                deletarGasto()
                
            
            case '5':
                gerar_excel()
            
            case '6':
                print("OK, SAINDO!")
                os._exit()
                
            
            case _:
                print('OPÇÃO INVÁLIDA.')
                pressioneParaContinuar()
                    
main()