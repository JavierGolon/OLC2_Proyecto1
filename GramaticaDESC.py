# importamos las herramientas de PLY
import ply.lex as lex
import ply.yacc as yacc
import ListaErrores as LErrores
entrada = ""
ListaE = LErrores.ListaError()
DatosGrafo = []

# ESTRUCTURA CON LAS PALABRAS RESERVADAS DE NUESTRO LENGUAJE

reservadas = {
    'if':'IF',
    'main':'MAIN',
    'print':'PRINT',
    'goto':'GOTO',
    'exit':'EXIT',
    'array':'ARRAY',
    'unset':'UNSET',
    'read':'READ',
    'int':'INT',
    'float':'FLOAT',
    'char':'CHAR',
    'abs':'ABS',
    'xor':'XOR'
}


tokens  = [
    'PTCOMA',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'RESIDUO',
    'ANDBIT',
    'ANDLOGICA',
    'MENOR',
    'MAYOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'NOIGUAL',
    'XORBIT',
    'ORBIT',
    'ORLOGICA',
    'SHIFTIZQ',
    'SHIFTDER',
    'NOTBIT',
    'NOTLOGICA',
    'DOSPUNTOS',
    'DECIMAL',
    'ENTERO',
    'TEMPORALES',
    'PARAMETROS',
    'DEVOLUCIONES',
    'RETORNONIVEL',
    'PILA',
    'SP',
    'CADENA',
    'ETIQUETA'
]+list(reservadas.values())

# DECLARACION DE LOS TOKENS
t_PTCOMA    = r';'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_RESIDUO   = r'%'
t_ANDBIT    = r'&'
t_ANDLOGICA =r'&&'
t_MENOR     = r'<'
t_MAYOR     = r'>'
t_MAYORIGUAL= r'>='
t_MENORIGUAL= r'<='
t_IGUALIGUAL  = r'=='
t_NOIGUAL = r'!='
t_XORBIT = r'\^'
t_ORBIT= r'\|' 
t_ORLOGICA= r'\|\|'
t_SHIFTIZQ=r'<<'
t_SHIFTDER=r'>>'
t_NOTBIT=r'~'
t_NOTLOGICA='!'
t_DOSPUNTOS=':'

# TOKENS CON EXPRESIONES REGULARES

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TEMPORALES(t):
    r"\$t(\d+)"
    t.type=reservadas.get(t.value.lower(),'TEMPORALES')
    return t
def t_PARAMETROS(t):
    r"\$a(\d+)"
    t.type=reservadas.get(t.value.lower(),'PARAMETROS')
    return t
def t_DEVOLUCIONES(t):
    r"\$v(\d+)"
    t.type=reservadas.get(t.value.lower(),'DEVOLUCIONES')
    return t
def t_RETORNONIVEL(t):
    r"\$ra"
    t.type=reservadas.get(t.value.lower(),'RETORNONIVEL')
    return t
def t_PILA(t):
    r"\$s(\d+)"
    t.type=reservadas.get(t.value.lower(),'PILA')
    return t
def t_ETIQUETA(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type=reservadas.get(t.value.lower(),'ETIQUETA')
    return t

def t_SP(t):
    r"\$sp"
    t.type=reservadas.get(t.value.lower(),'SP')
    return t

def t_CADENA(t):
    r'(\'|\").*?(\'|\")'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    
def t_error(t):
    
    print("Illegal character '%s'" % t.value[0])
    mistake=LErrores.Error('Lexical Error',str(t.value[0]),'Ilegal Character',t.lexer.lineno,find_column(entrada,t))
    ListaE.AddError(mistake)
    t.lexer.skip(1)     

lexer = lex.lex()

#================================================== GRAMATICA =============================================================
#importamos las clases con las instrucciones y las expresiones(Nodos)
from Expresiones import *
from Instrucciones import * 
# declaracion de las precedencias
precedence = (
    ('left','XOR'),
    ('left','ORLOGICA'),
    ('left','ANDLOGICA'),
    ('left','ORBIT'),
    ('left','XORBIT'),
    ('left','ANDBIT'),
    ('left','NOTBIT'),
    ('nonassoc','MAYOR','MENOR','MAYORIGUAL','MENORIGUAL','NOIGUAL','IGUALIGUAL'),
    ('left','SHIFTIZQ','SHIFTDER'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO','RESIDUO'),
    ('right','NOTLOGICA'),
    ('right','UMENOS'),
    )

#================================== DEFINICION DE LA GRAMATICA =================================================================
 
def p_init(t):
    'init  :    MAIN DOSPUNTOS listainstrucciones'
    t[0]=t[3]
    DatosGrafo.append('init  :    MAIN DOSPUNTOS listainstrucciones {t[0]=t[3]}')

def p_lista_instrucciones(t):
    'listainstrucciones :   simpleinstrucciones listainstruccionesp'
    t[0]=t[2]
    DatosGrafo.append('listainstrucciones :   listainstrucciones simpleinstrucciones { t[0]=t[2]}')

def p_lista_instrucciones_prima(t):
    'listainstruccionesp : simpleinstrucciones listainstruccionesp'
    t[0] = t[2]
    t[0].insert(0,t[-1])
    DatosGrafo.append('listainstrucciones : simpleinstrucciones {t[0] = t[2] t[0].insert(0,t[-1])}')

def p_lista_instrucciones_epsilon(t):
    'listainstruccionesp    :   '
    t[0] = [t[-1]]
    DatosGrafo.append('listainstruccionesp  :   epsilon {t[0] = [t[-1]]}')


def p_simpleinstrucciones(t):
    '''simpleinstrucciones    : declaracion
                              | asignacion
                              | ifcomando
                              | exit
                              | print
                              | etiqueta
                              | goto
                              | unset'''
    t[0]=t[1]
    DatosGrafo.append('simpleinstrucciones :  Comandos t[0]=t[1] ')

def p_declaracion(t):
    'declaracion   :    variable PTCOMA'
    t[0]=declaracion(t[1])
    DatosGrafo.append('declaracion   :    variable PTCOMA { t[0]=declaracion(t[1])}')

def p_asignacion(t):
    'asignacion :   variable IGUAL tipo PTCOMA'
    t[0]=asignacion(t[1],t[3])
    DatosGrafo.append('asignacion :   variable IGUAL tipo PTCOMA {t[0]=asignacion(t[1],t[3])}')


def p_tipo(t):
    '''tipo :   instruccionregistro
            |   conversion
            |   arreglo'''
    t[0]=t[1]
    DatosGrafo.append('tipo :   cambiartipos {t[0]=t[1]}')

def p_variable(t):
    '''variable :   TEMPORALES
                |   PARAMETROS
                |   DEVOLUCIONES
                |   RETORNONIVEL
                |   PILA
                |   SP'''
    t[0]=ExpresionVariable(t[1])
    DatosGrafo.append('variable :   misvaiable {t[0]=ExpresionVariable(t[1])}')

def p_variable_arreglo(t):
    '''variable :   TEMPORALES listadimension
                |   PARAMETROS listadimension
                |   DEVOLUCIONES listadimension
                |   RETORNONIVEL listadimension
                |   PILA listadimension
                |   SP listadimension'''
    t[0]=ExpresionArreglo(t[1],t[2])
    DatosGrafo.append('variable :   misvaiable dimensional {t[0]=ExpresionArreglo(t[1],t[2])}')

def p_instruccionregistro(t):        
    '''instruccionregistro  : registro operacion registro'''
    if t[2] == '+'  : t[0]=ExpresionBinariaAritmetica(t[1],t[3],OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0]=ExpresionBinariaAritmetica(t[1],t[3],OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0]=ExpresionBinariaAritmetica(t[1],t[3],OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0]=ExpresionBinariaAritmetica(t[1],t[3],OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%': t[0]=ExpresionBinariaAritmetica(t[1],t[3],OPERACION_ARITMETICA.RESIDUO)
    elif t[2] == '&&': t[0]=ExpresionBinarioLogica(t[1],t[3],OPERACION_LOGICA.AND)
    elif t[2] == '||': t[0]=ExpresionBinarioLogica(t[1],t[3],OPERACION_LOGICA.OR)
    elif t[2] == 'xor': t[0]=ExpresionBinarioLogica(t[1],t[3],OPERACION_LOGICA.XOR)
    elif t[2] == '&': t[0]=ExpresionBinariaBit(t[1],t[3],OPERACION_BIT.AND)
    elif t[2] == '|': t[0]=ExpresionBinariaBit(t[1],t[3],OPERACION_BIT.OR)
    elif t[2] == '^': t[0]=ExpresionBinariaBit(t[1],t[3],OPERACION_BIT.XOR)
    elif t[2] == '<<': t[0]=ExpresionBinariaBit(t[1],t[3],OPERACION_BIT.SHIFTIZQ)
    elif t[2] == '>>': t[0]=ExpresionBinariaBit(t[1],t[3],OPERACION_BIT.SHIFTDER)
    elif t[2] == '==': t[0]=ExpresionBinariaRelacional(t[1],t[3],OPEREACION_RELACIONAL.IGUAL)
    elif t[2] == '!=': t[0]=ExpresionBinariaRelacional(t[1],t[3],OPEREACION_RELACIONAL.DIFERENTE)
    elif t[2] == '>=': t[0]=ExpresionBinariaRelacional(t[1],t[3],OPEREACION_RELACIONAL.MAYORIGUAL)
    elif t[2] == '<=': t[0]=ExpresionBinariaRelacional(t[1],t[3],OPEREACION_RELACIONAL.MENORIGUAL)
    elif t[2] == '>': t[0]=ExpresionBinariaRelacional(t[1],t[3],OPEREACION_RELACIONAL.MAYOR) 
    elif t[2] == '<': t[0]=ExpresionBinariaRelacional(t[1],t[3],OPEREACION_RELACIONAL.MENOR)
    DatosGrafo.append('instruccionregistro : registro '+str(t[2])+' registro {if t[2] is operand, make decision}')  
def p_operacion(t):
    '''operacion            :  MAS 
                            |  MENOS  
                            |  POR  
                            |  DIVIDIDO  
                            |  RESIDUO  
                            |  ANDLOGICA 
                            |  ORLOGICA  
                            |  XOR  
                            |  ANDBIT 
                            |  ORBIT  
                            |  XORBIT  
                            |  SHIFTIZQ  
                            |  SHIFTDER  
                            |  IGUALIGUAL 
                            |  NOIGUAL  
                            |  MAYORIGUAL  
                            |  MENORIGUAL  
                            |  MAYOR  
                            |  MENOR '''
    t[0] = t[1]
    DatosGrafo.append('operacion :  '+str(t[1])+' {t[0]=t[1]}')  


def p_instruccion_registrounico(t):
    '''instruccionregistro  : registro'''
    t[0]=t[1]
    DatosGrafo.append('instruccionregistro  : registro {t[0]=t[1]}')

def p_registro_parentesis(t):
    '''registro :   PARIZQ registro PARDER'''
    t[0] = t[2]
    DatosGrafo.append('registro :   PARIZQ registro PARDER {t[0] = t[2]}')


def p_instruccionregistro_diferentes(t):
    '''registro  : ABS PARIZQ registro PARDER 
                            | NOTLOGICA registro 
                            | NOTBIT registro
                            | MENOS registro %prec UMENOS
                            | ANDBIT registro'''
    if t[1] == '!': t[0]=ExpresionMonoLogica(t[2],OPERACION_LOGICA.NOT)
    elif t[1] == '~': t[0]=ExpresionMonoBit(t[2],OPERACION_BIT.NOT)
    elif t[1] == '-': t[0]=ExpresionNegativo(t[2])
    elif t[1] == 'abs': t[0]=ExpresionAbs(t[3])
    elif t[1] == '&' : t[0] =ExpresionReferencia(t[2])
    DatosGrafo.append('registro : '+str(t[1]))  
def p_nuevo_(t):
    'registro   :   readisntr'
    t[0]=t[1]

def p_registro(t):
    '''registro :   ENTERO
                |   DECIMAL'''
    t[0]=ExpresionNumero(t[1])
    DatosGrafo.append('registro :   ENTERO {t[0]=ExpresionNumero(t[1])}') 

def p_registro_cadena(t):
    '''registro :   CADENA'''
    t[0]=ExpresionComillas(t[1])
    DatosGrafo.append('registro :   CADENA {t[0]=ExpresionComillas(t[1])}') 

def p_registro_acceso(t):
    '''registro :   acceso'''
    t[0]=t[1]
    DatosGrafo.append('registro :   acceso { t[0]=t[1]}') 
                
def p_acceso(t):
    '''acceso   :   variable'''
    t[0]=t[1]
    DatosGrafo.append('registro :   variable {[0]=t[1]}') 


def p_lista_dimension(t):
    '''listadimension    :   dimension listadimensionp'''
    t[0] = t[2]
    DatosGrafo.append('listadimension    :   dimension listadimensionp { t[0] = t[2]}')

def p_lista_dimension_prima(t):
    ''' listadimensionp :   dimension listadimensionp''' 
    t[0] = t[2]
    t[0].insert(0,t[-1])
    DatosGrafo.append('listadimension    :   dimension listadimensionp {t[0] = t[2] t[0].insert(0,t[-1])}')

def p_listadimension_epsilon(t):
    '''listadimensionp   :  '''
    t[0] = [t[-1]]
    DatosGrafo.append('listadimension   :    {t[0] = [t[-1]]}')

def p_dimension(t):
    '''dimension    :   CORCHETEIZQ registro CORCHETEDER'''
    t[0] = ExpresionDimension(t[2])
    DatosGrafo.append('dimension    :   CORCHETEIZQ registro CORCHETEDER { t[0] = ExpresionDimension(t[2])}')



#=============================================================================================================================================================
  #====================================================================================================== DESC SIN CAMBIOS ====================================
  #============================================================================================================================================================
# ====================== Gramatica Para las Palabras Reservadas y funciones especiales

def p_conversion(t):
    'conversion   : PARIZQ eltipo PARDER registro'
    t[0]=Casteo(t[2],t[4])
    DatosGrafo.append('conversion   : PARIZQ eltipo PARDER registro {t[0]=Casteo(t[2],t[4])}')



def p_eltipo(t):
    '''eltipo   :   FLOAT
                |   INT
                |   CHAR'''
    t[0]=t[1]
    DatosGrafo.append('eltipo   :   FLOAT {t[0]=t[1]}')

def p_arreglo(t):
    'arreglo    :   ARRAY PARIZQ PARDER'
    t[0]=Arreglo(2,2)
    DatosGrafo.append('arreglo    :   ARRAY PARIZQ PARDER {t[0]=Arreglo(2,2)}')   

def p_exit(t):
    'exit   :   EXIT PTCOMA'
    t[0]=Exit(t[1])
    DatosGrafo.append('exit   :   EXIT PTCOMA {t[0]=Exit(t[1])}')
def p_print(t):
    'print  : PRINT PARIZQ registro PARDER PTCOMA'
    t[0]=Imprimir(t[3])
    DatosGrafo.append('print  : PRINT PARIZQ registro PARDER PTCOMA {t[0]=Imprimir(t[3])}')

def p_etiqueta(t):
    'etiqueta   :  ETIQUETA DOSPUNTOS' #
    t[0]=Etiqueta(t[1])
    DatosGrafo.append('etiqueta   :  ETIQUETA DOSPUNTOS { t[0]=Etiqueta(t[1])}') 
def p_goto(t):
    'goto   :   GOTO ETIQUETA PTCOMA' #
    t[0]=Goto(t[2])
    DatosGrafo.append('goto   :   GOTO ETIQUETA PTCOMA {t[0]=Goto(t[2])}')


def p_read(t):
    'readisntr   :   READ PARIZQ PARDER '
    t[0]=Read(t[1])
    DatosGrafo.append('read   :   READ PARIZQ PARDER {t[0]=Read(t[1])}')

def p_unset(t):
    'unset  :   UNSET PARIZQ acceso PARDER PTCOMA'
    t[0]=Unset(t[3])
    DatosGrafo.append('unset  :   UNSET PARIZQ acceso PARDER PTCOMA {t[0]=Unset(t[3])}')

def p_if(t):
    'ifcomando :    IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA'
    t[0]=instruccionIf(t[3],t[6])
    DatosGrafo.append('ifcomando : IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA {t[0]=instruccionIf(t[3],t[6])}')



def p_error(t):
    if t:
        print("Syntax error at token", t.type)
        # Just discard the token and tell the parser it's okay.
        mistake=LErrores.Error('Sintax Error',str(t.value),t.type,t.lexer.lineno,find_column(entrada,t))
        ListaE.AddError(mistake)
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()



# Funcion que corre nuestro parse
def parse(input) :

    entrada=input
    return parser.parse(input)
