import Gramatica as g
import TablaSimbolos as TS
from operator import xor
from Expresiones import *
from Instrucciones import * 

def accion_imprimir(instr,ts):
    registro = resolver_Expresion(instr.cadena,ts)
    print('>> ', registro)

def accion_declaracion(inst,ts):
    searched_var = ts.obtener(inst.variable)
    if searched_var is None:
        simbolo = TS.Simbolo(inst.variable,TS.TIPO_DATO.NUMERO,0) # lo inicializo en 0
        ts.agregar(simbolo) # crea una nueva variable en la tabla de simbolos


def accion_asignar(instr,ts):
    valor = resolver_Expresion(instr.valor,ts)
    id = Obtener_o_Crear_Id(instr.variable,ts)
    # una vez comprobada ya esta creada la var o verificada
    if type(valor) is str:
        simbolo=TS.Simbolo(id,TS.TIPO_DATO.CADENA,valor) # le asigno ya el nuevo valor
    elif type(valor) is int:
        simbolo=TS.Simbolo(id,TS.TIPO_DATO.NUMERO,valor) # le asigno ya el nuevo valor
    elif type(valor) is float:
        simbolo=TS.Simbolo(id,TS.TIPO_DATO.FLOAT,valor) # le asigno ya el nuevo valor
    ts.actualizar(simbolo)

def Obtener_o_Crear_Id(variable,ts):
    searched_var = ts.obtener(variable)
    if searched_var is None:
        simbolo = TS.Simbolo(variable,TS.TIPO_DATO.NUMERO,0) # lo inicializo en 0
        ts.agregar(simbolo) # crea una nueva variable en la tabla de simbolos
    return variable


def resolver_Expresion(Expresion,ts):
    if isinstance(Expresion,ExpresionBinariaAritmetica):
        izq = resolver_Expresion(Expresion.exp1,ts)
        der = resolver_Expresion(Expresion.exp2,ts)
        try:
            if Expresion.operador == OPERACION_ARITMETICA.MAS :
                if type(izq) is str == type(der) is str:
                    return izq + der
                elif (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq) + int(der)
            elif Expresion.operador == OPERACION_ARITMETICA.MENOS:
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq) - int(der)
            elif Expresion.operador == OPERACION_ARITMETICA.POR:
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq) * int(der)
            elif Expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq) / int(der)
            elif Expresion.operador == OPERACION_ARITMETICA.RESIDUO:
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq) % int(der)
        except:
            print('Error en el tipo de conversion')

    elif isinstance(Expresion,ExpresionBinariaRelacional):
        izq = resolver_Expresion(Expresion.exp1,ts)
        der = resolver_Expresion(Expresion.exp2,ts)
        #========================================= OPERACIONES BINARIAS RELACIONALES ==========================
        try:
            if Expresion.operador == OPEREACION_RELACIONAL.IGUAL :
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq==der)
                elif (type(izq) is str) and (type(der) is str):
                    return int(izq==der)
            if Expresion.operador == OPEREACION_RELACIONAL.DIFERENTE :
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq!=der)
                elif (type(izq) is str) and (type(der) is str):
                    return int(izq!=der)
            if Expresion.operador == OPEREACION_RELACIONAL.MAYORIGUAL :
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq>=der)
                elif (type(izq) is str) and (type(der) is str):
                    return int(izq>=der)
            if Expresion.operador == OPEREACION_RELACIONAL.MENORIGUAL :
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq<=der)
                elif (type(izq) is str) and (type(der) is str):
                    return int(izq<=der)
            if Expresion.operador == OPEREACION_RELACIONAL.MAYOR :
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq>der)
                elif (type(izq) is str) and (type(der) is str):
                    return int(izq>der)
            if Expresion.operador == OPEREACION_RELACIONAL.MENOR :
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq<der)
                elif (type(izq) is str) and (type(der) is str):
                    return int(izq<der)
        except :
            print('Error en el tipo de conversion')
    #================================================== OPERACIONES LOGICAS BINARIAS ================================

    elif isinstance(Expresion,ExpresionBinarioLogica): # no importa tipo de dato
        izq = resolver_Expresion(Expresion.exp1,ts)
        der = resolver_Expresion(Expresion.exp2,ts)

        if Expresion.operador == OPERACION_LOGICA.AND :
            return bool(izq) and bool(der)
        elif Expresion.operador == OPERACION_LOGICA.OR :
            return bool(izq) or bool(der)
        elif Expresion.operador == OPERACION_LOGICA.XOR :
            return bool(izq) or bool(der)
        elif Expresion.operador == OPERACION_LOGICA.XOR :
            return xor(bool(izq),bool(der))
    #============================== OPERACIONES BINARIAS BIT ========================


    elif isinstance(Expresion,ExpresionBinariaBit): # tiene try solo opera numeros
        izq = resolver_Expresion(Expresion.exp1,ts)
        der = resolver_Expresion(Expresion.exp2,ts)
        try:
            if(Expresion.operador ==OPERACION_BIT.AND):
                return izq & der
            elif(Expresion.operador ==OPERACION_BIT.OR):
                return izq | der
            elif(Expresion.operador ==OPERACION_BIT.XOR):
                return izq ^ der
            elif(Expresion.operador ==OPERACION_BIT.SHIFTIZQ):
                return izq << der
            elif(Expresion.operador ==OPERACION_BIT.SHIFTDER):
                return izq >> der
        except:
            print('Error en el tipo de conversion')
        
    #================================================ MONO ===========================================        
    elif isinstance(Expresion,ExpresionMonoLogica):
        return not bool(resolver_Expresion(Expresion.exp,ts))
    elif isinstance(Expresion,ExpresionMonoBit):
        return ~ bool(resolver_Expresion(Expresion.exp,ts))
    elif isinstance(Expresion,ExpresionNumero):
        return Expresion.valor
    elif isinstance(Expresion,ExpresionComillas):
        return Expresion.valor
    elif isinstance(Expresion,ExpresionNegativo):
        exp = resolver_Expresion(Expresion.exp,ts)
        return exp*-1
    elif isinstance(Expresion,ExpresionAbs):
        exp = resolver_Expresion(Expresion.exp,ts)
        return abs(exp)
    elif isinstance(Expresion,ExpresionVariable):
        return ts.obtener(Expresion.registro).valor

#===================================== Acciones especiales ==================================================
def accion_exit(inst,ts):
    pass
def accion_unset(inst,ts):
    
    pass
def accion_read(inst,ts):
    pass 
def accion_if(inst,ts):

    pass
def accion_etiqueta(inst,ts,posicion):
    searched_var = ts.obtener(inst.iden)
    if searched_var is None:
        simbolo = TS.Simbolo(inst.iden,TS.TIPO_DATO.METODO,posicion) # lo inicializamos en metodo
        ts.agregar(simbolo) # agregamos la etiqueta a la tabla de simbolos


def Recorrer_Instrucciones(instrucciones,ts):
    largo = len(instrucciones)
    print('len-->',largo)
    for i in range(0,largo,1):
        if isinstance(instrucciones[i],Imprimir): accion_imprimir(instrucciones[i],ts)
        elif isinstance(instrucciones[i],asignacion): accion_asignar(instrucciones[i],ts)
        elif isinstance(instrucciones[i],declaracion): accion_declaracion(instrucciones[i],ts)
        elif isinstance(instrucciones[i],Exit): accion_exit(instrucciones[i],ts)
        elif isinstance(instrucciones[i],Unset): accion_unset(instrucciones[i],ts)
        elif isinstance(instrucciones[i],Read): accion_read(instrucciones[i],ts)
        elif isinstance(instrucciones[i],instruccionIf): accion_if(instrucciones[i],ts)
        elif isinstance(instrucciones[i],Etiqueta): accion_etiqueta(instrucciones[i],ts,1)
        elif isinstance(instrucciones[i],Goto): 
            print('salto')
        else: print('Error: La instruccion encontrada es invalida')

#======== Llamada del archivo de entrada(Temporal, tiene que  hacerser con el text de la interfaz) ======
file = open("./entrada.txt", "r")
input = file.read()
instrucciones = g.parse(input)
ts_global=TS.TablaDeSimbolos()
Recorrer_Instrucciones(instrucciones,ts_global)

