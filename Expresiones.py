from enum import Enum

class OPERACION_ARITMETICA(Enum):
    MAS=1
    MENOS=2
    DIVIDIDO=3
    POR=4
    RESIDUO=5
    ABSOLUTO=6
class OPERACION_LOGICA(Enum):
    NOT=1
    AND=2
    OR=3
    XOR=4

class OPERACION_BIT(Enum):
    NOT=1
    AND=2
    OR=3
    XOR=4
    SHIFTIZQ=5
    SHIFTDER=6

class OPEREACION_RELACIONAL(Enum):
    IGUAL=1
    DIFERENTE=2
    MAYORIGUAL=3
    MENORIGUAL=4
    MAYOR=5
    MENOR=6

class ExpresionNumerica:
    ''' clase maestra que representa una expresion numerica'''
class ExpresionLogica:
    ''' clase que representa una expresion logica'''
class ExpresionBit:
    ''' clase que representa una expresion logica'''
class ExpresionRelacional:
    ''' clase que representa una expresion logica'''

class ExpresionBinariaRelacional(ExpresionRelacional):
    def __init(self,exp1,exp2,operador):
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

class ExpresionBinariaBit(ExpresionBit):
    def __init(self,exp1,exp2,operador):
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

class ExpresionBinarioLogica(ExpresionLogica):
    def __init(self,exp1,exp2,operador):
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

class ExpresionBinariaAritmetica(ExpresionNumerica):
    def __init(self,exp1,exp2,operador):
        self.exp1=exp1
        self.exp2=exp2
        self.operador=operador

class ExpresionMonoLogica(ExpresionLogica):
    def __init__(self,exp,operador):
        self.exp=exp
        self.operador=operador
class ExpresionMonoBit(ExpresionBit):
    def __init__(self,exp,operador):
        self.exp=exp
        self.operador=operador
class ExpresionNegativo(ExpresionNumerica):
    def __init__(self,exp):
        self.exp=exp

class ExpresionAbs(ExpresionNumerica):
    def __init__(self,exp):
        self.exp=exp

class ExpresionNumero(ExpresionNumerica):
    ''' esta clase representa como tal el numero (Entero o decimal) '''
    def __init__(self,valor=0):
        self.valor=valor
class ExpresionVariable():
    ''' esta clase representa como tal un registro'''
    def __init__(self,registro=""):
        self.registro=registro
class ExpresionCadena:
    ''' Representa una clase que contiene todas las expresiones de tipo cadena'''

class ExpresionComillas(ExpresionCadena):
    def __init__(self,valor):
        self.valor=valor


