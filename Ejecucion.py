import Gramatica as g
import TablaSimbolos as TS

from Expresiones import *
from Instrucciones import * 

def accion_imprimir(instr,ts):
    print('Estoy en imprimir')

def Recorrer_Instrucciones(instrucciones,ts):
    
    for inst in instrucciones:
        if isinstance(inst,Imprimir): accion_imprimir(inst,ts)
        else: print('Error: La instruccion encontrada es invalida')

#======== Llamada del archivo de entrada(Temporal, tiene que  hacerser con el text de la interfaz) ======
file = open("./entrada.txt", "r")
input = file.read()
instrucciones = g.parse(input)
ts_global=TS.TablaDeSimbolos()
Recorrer_Instrucciones(instrucciones,ts_global)
