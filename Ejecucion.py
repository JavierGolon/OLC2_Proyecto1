import Gramatica as g
import TablaSimbolos as TS
from operator import xor
from Expresiones import *
from Instrucciones import * 
from GraficarAST import Graficadora
#sys.setrecursionlimit()
#sys.setrecursionlimit(3000)
""" >>> Accion Imprimir Correcta """
def accion_imprimir(instr,ts):
    # en print solo puedo obtener valores de registros
    registro = Obtener_Valor_Registro(instr.cadena,ts)
    if registro is None:
        print('>> ','Error, Referencia Erronea -- Print()')
    else:
        print('>> ', registro.valor)

""" >>> Accion Obtener Valor registro Correcta """
def Obtener_Valor_Registro(registro,ts):
    valor = ts.obtener(registro.registro)
    return valor

""" >>> Accion Declaracion Correcta """
def accion_declaracion(inst,ts):
    searched_var = ts.obtener(inst.variable)
    if searched_var is None:
        simbolo = TS.Simbolo(TS.TIPO_DATO.NUMERO,0) # lo inicializo en 0
        ts.agregar(simbolo,inst.variable) # crea una nueva variable en la tabla de simbolos


def accion_asignar(instr,ts):
    if isinstance(instr.valor,ExpresionReferencia):
        simboloref = ts.ObtenerTabla()[instr.valor.registro.registro]
        ts.agregar(simboloref,instr.variable)
    else:
        valor = resolver_Expresion(instr.valor,ts) # Obtenie la operacion de la expresion
        id = Obtener_o_Crear_Id(instr.variable,ts)
        # una vez comprobada ya esta creada la var o verificada
        if type(valor) is str:
            simbolo=TS.Simbolo(TS.TIPO_DATO.CADENA,valor) # le asigno ya el nuevo valor
        elif type(valor) is int:
            simbolo=TS.Simbolo(TS.TIPO_DATO.NUMERO,valor) # le asigno ya el nuevo valor
        elif type(valor) is float:
            simbolo=TS.Simbolo(TS.TIPO_DATO.FLOAT,valor) # le asigno ya el nuevo valor
        ts.actualizar(simbolo,id)

""" >>> Accion Crear Variable o Verificar Registro en Ts Correcta """
def Obtener_o_Crear_Id(variable,ts):
    searched_var = ts.obtener(variable)
    if searched_var is None: # creamos variable
        simbolo = TS.Simbolo(TS.TIPO_DATO.NUMERO,0) # lo inicializo en 0
        ts.agregar(simbolo,variable) # crea una nueva variable en la tabla de simbolos
    return variable # solo retorno de mas el nombre


def resolver_Expresion(Expresion,ts):

    if isinstance(Expresion,ExpresionBinariaAritmetica):
        izq = resolver_Expresion(Expresion.exp1,ts) # nunca vienen expresiones recursivas solo 2 llamadas
        der = resolver_Expresion(Expresion.exp2,ts) # unico caso es en acceso a arreglos
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
                    if izq == 0:
                        return '@400@'
                    else:
                        return round(int(izq) / int(der),1)
            elif Expresion.operador == OPERACION_ARITMETICA.RESIDUO:
                if (type(izq) is int or type(izq) is float) and (type(der) is int or type(der) is float):
                    return int(izq) % int(der)
        except Exception as ext:
            print('Error,',ext)
            return '@400@'

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
        except Exception as ext:
            print('Error,',ext)
            return '@400@'
    #================================================== OPERACIONES LOGICAS BINARIAS ================================

    elif isinstance(Expresion,ExpresionBinarioLogica): # no importa tipo de dato igual coloco try cath
        izq = resolver_Expresion(Expresion.exp1,ts)
        der = resolver_Expresion(Expresion.exp2,ts)
        
        try:
            if Expresion.operador == OPERACION_LOGICA.AND :
                return bool(izq) and bool(der)
            elif Expresion.operador == OPERACION_LOGICA.OR :
                return bool(izq) or bool(der)
            elif Expresion.operador == OPERACION_LOGICA.XOR :
                return xor(bool(izq),bool(der))

        except Exception as ext:
            print('Error,',ext)
            return '@400@'
        
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
        return int (not bool(resolver_Expresion(Expresion.exp,ts)))
    elif isinstance(Expresion,ExpresionMonoBit):
        exp = resolver_Expresion(Expresion.exp,ts)
        if type(exp) is int or type(exp)  is float:
            return (~int(exp))
        else:
            return "@400@"
    elif isinstance(Expresion,ExpresionNumero):
        return Expresion.valor
    elif isinstance(Expresion,ExpresionComillas):
        return Expresion.valor
    elif isinstance(Expresion,ExpresionNegativo):
        exp = resolver_Expresion(Expresion.exp,ts)
        if type(exp) is int or type(exp) is float:
            return exp*-1
        else:
            return "@400@"
    elif isinstance(Expresion,ExpresionAbs):
        exp = resolver_Expresion(Expresion.exp,ts)
        if type(exp) is int or type(exp) is float:
            return abs(exp)
        else:
            return "@400@"
    elif isinstance(Expresion,ExpresionVariable):
        valor = ts.obtener(Expresion.registro)
        if valor is None:
            return "@400@"
        else:
            return valor.valor
    #================= Instancias de los Casteos o de la declaracion de arreglo (FALTA ARREGLOS) ======================
    elif isinstance(Expresion,Arreglo):
        pass
    elif isinstance(Expresion,Casteo):
        tipo = Expresion.tipo
        valor =resolver_Expresion(Expresion.valor,ts)
        if tipo == 'int':
            if type(valor) is str and valor != '':
                return int(ord(valor[0]))
            elif type(valor) is int or type(valor) is float:
                return  int(valor)
        elif tipo =='float':
            if type(valor) is str and valor != '':
                return float(int(ord(valor[0])))
            elif type(valor) is int or type(valor) is float:
                return  float(valor)
        elif tipo == 'char':
            if type(valor) is str and valor != '':
                return valor[0]
            elif type(valor) is int or type(valor) is float:
                if valor > 255:
                    return str(chr(int(valor)%256))
                elif valor > 0 and valor <=255:
                    return str(chr(int(valor)))
    elif isinstance(Expresion,Read):
        valorconsola = 'cambiar'
        return valorconsola
    

#===================================== Acciones especiales ==================================================
def accion_unset(inst,ts):
    ts.EliminarSimbolo(inst.registro)
    pass

def accion_etiqueta(inst,ts,posicion):
    searched_var = ts.obtener(inst.iden)
    if searched_var is None:
        simbolo = TS.Simbolo(TS.TIPO_DATO.ETIQUETA,posicion) # lo inicializamos en metodo
        ts.agregar(simbolo,inst.iden) # agregamos la etiqueta a la tabla de simbolos



def accion_LlenarTsEtiquetas(instrucciones,ts):
    size = len(instrucciones)
    i = 0
    lastflagnane = ""
    flagetiq = False
    while(i<size):
        if isinstance(instrucciones[i],Etiqueta):
            accion_etiqueta(instrucciones[i],ts,i)
            lastflagnane = instrucciones[i].iden
            flagetiq=True
        if isinstance(instrucciones[i],declaracion):
            var = instrucciones[i].variable
            if '$a' in var:
                if flagetiq is True:
                    lastindex = ts.obtener(lastflagnane).valor
                    simbolo=TS.Simbolo(TS.TIPO_DATO.METODO,lastindex)
                    ts.actualizar(simbolo,lastflagnane)
                    
            elif '$v' in var:
                if flagetiq is True:
                    lastindex = ts.obtener(lastflagnane).valor
                    simbolo=TS.Simbolo(TS.TIPO_DATO.FUNCION,lastindex)
                    ts.actualizar(simbolo,lastflagnane)
                    
        if isinstance(instrucciones[i],asignacion):
            var = instrucciones[i].variable
            if '$a' in var:
                if flagetiq is True:
                    lastindex = ts.obtener(lastflagnane).valor
                    simbolo=TS.Simbolo(TS.TIPO_DATO.METODO,lastindex)
                    ts.actualizar(simbolo,lastflagnane)
                    
            elif '$v' in var:
                if flagetiq is True:
                    lastindex = ts.obtener(lastflagnane).valor
                    simbolo=TS.Simbolo(TS.TIPO_DATO.FUNCION,lastindex)
                    ts.actualizar(simbolo,lastflagnane)
                    
        if isinstance(instrucciones[i],Goto):
            pass
        i+=1


def Recorrer_Instrucciones(instrucciones,ts):
    accion_LlenarTsEtiquetas(instrucciones,ts) # mando a llenar la ts con todas mis etiquetas
    largo = len(instrucciones)
    i = 0
    while i < largo:
        if isinstance(instrucciones[i],Imprimir): accion_imprimir(instrucciones[i],ts)
        elif isinstance(instrucciones[i],asignacion): accion_asignar(instrucciones[i],ts)
        elif isinstance(instrucciones[i],declaracion): accion_declaracion(instrucciones[i],ts)
        elif isinstance(instrucciones[i],Unset): accion_unset(instrucciones[i].registro,ts)
        elif isinstance(instrucciones[i],instruccionIf): 
            estado = resolver_Expresion(instrucciones[i].exprelogica,ts)
            if estado == 0 :
                ''' sigue el flujo del programa '''
            elif estado == 1:
                newindex = ts.obtener(instrucciones[i].goto).valor # la etiqueta fijo esta en ts
                i= newindex # salto a la posicion donde viene la etiqueta para hacer los saltos
                continue 
        elif isinstance(instrucciones[i],Goto):
            newindex = ts.obtener(instrucciones[i].label).valor #la etiqueta fijo esta en ts
            i=newindex
            continue
        elif isinstance(instrucciones[i],Exit):
            i = largo+1 # termina la ejecucion de mi codigo
            continue
        i+=1

#======== Llamada del archivo de entrada(Temporal, tiene que  hacerser con el text de la interfaz) ======
file = open("./entrada.txt", "r")
input = file.read()
instrucciones = g.parse(input)
ts_global=TS.TablaDeSimbolos()
Recorrer_Instrucciones(instrucciones,ts_global)
for i in ts_global.ObtenerTabla():
    print(i)
    print('--',ts_global.ObtenerTabla()[i].tipo,'--',ts_global.ObtenerTabla()[i].valor)
"""
grafo = Graficadora()
grafo.Recorrer_Instrucciones_Inicio(instrucciones)"""