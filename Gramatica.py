# importamos las herramientas de PLY
import ply.lex as lex
import ply.yacc as yacc

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
    r'\'.*?\''
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
    t.lexer.skip(1)     

lexer = lex.lex()

"""
f = open("./entrada.txt", "r")
input = f.read()
lexer.input(input)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)"""
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

def p_lista_instrucciones(t):
    'listainstrucciones :   listainstrucciones simpleinstrucciones'
    t[1].append(t[2])
    t[0]=t[1]

def p_lista_instrucciones_simple(t):
    'listainstrucciones : simpleinstrucciones'
    t[0]=[t[1]]
def p_simpleinstrucciones(t):
    '''simpleinstrucciones    : declaracion
                              | asignacion
                              | ifcomando
                              | exit
                              | print
                              | etiqueta
                              | goto
                              | read
                              | unset'''
    t[0]=t[1]
def p_declaracion(t):
    'declaracion   :    variable PTCOMA'
    t[0]=t[1]
def p_asignacion(t):
    'asignacion :   variable IGUAL tipo PTCOMA'
    t[0]=asignacion(t[1],t[3])
def p_tipo(t):
    '''tipo :   instruccionregistro
            |   conversion
            |   ARRAY PARIZQ PARDER'''
    t[0]=t[1]
def p_variable(t):
    '''variable :   TEMPORALES
                |   PARAMETROS
                |   DEVOLUCIONES
                |   RETORNONIVEL
                |   PILA
                |   SP'''
    t[0]=t[1]
def p_instruccionregistro(t):        
    '''instruccionregistro  : registro MAS registro
                            | registro MENOS registro 
                            | registro POR registro 
                            | registro DIVIDIDO registro 
                            | registro RESIDUO registro 
                            | registro ANDLOGICA registro
                            | registro ORLOGICA registro 
                            | registro XOR registro 
                            | registro ANDBIT registro
                            | registro ORBIT registro 
                            | registro XORBIT registro 
                            | registro SHIFTIZQ registro 
                            | registro SHIFTDER registro 
                            | registro IGUALIGUAL registro
                            | registro NOIGUAL registro 
                            | registro MAYORIGUAL registro 
                            | registro MENORIGUAL registro 
                            | registro MAYOR registro 
                            | registro MENOR registro'''
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
    elif t[2] == '==': t[0]=ExpresionRelacional(t[1],t[3],OPEREACION_RELACIONAL.IGUAL)
    elif t[2] == '!=': t[0]=ExpresionRelacional(t[1],t[3],OPEREACION_RELACIONAL.DIFERENTE)
    elif t[2] == '>=': t[0]=ExpresionRelacional(t[1],t[3],OPEREACION_RELACIONAL.MAYORIGUAL)
    elif t[2] == '<=': t[0]=ExpresionRelacional(t[1],t[3],OPEREACION_RELACIONAL.MENORIGUAL)
    elif t[2] == '>': t[0]=ExpresionRelacional(t[1],t[3],OPEREACION_RELACIONAL.MAYOR) 
    elif t[2] == '<': t[0]=ExpresionRelacional(t[1],t[3],OPEREACION_RELACIONAL.MENOR)  
    

def p_instruccionregistro_diferentes(t):
    '''instruccionregistro  : ABS PARIZQ registro PARDER 
                            | NOTLOGICA registro 
                            | NOTBIT registro
                            | MENOS registro %prec UMENOS'''
    if t[1] == '!': t[0]=ExpresionBinarioLogica(t[2],OPERACION_LOGICA.NOT)
    elif t[1] == '~': t[0]=ExpresionMonoBit(t[2],OPERACION_BIT.NOT)
    elif t[1] == '-': t[0]=ExpresionNegativo(t[2])
    elif t[1] == 'abs': t[0]=ExpresionAbs(t[3])
def p_instruccion_registrounico(t):
    '''instruccionregistro  : registro'''
    t[0]=t[1]

def p_registro(t):
    '''registro :   ENTERO
                |   DECIMAL'''
    t[0]=ExpresionNumero(t[1])

def p_registro_cadena(t):
    '''registro :   CADENA'''
    t[0]=ExpresionComillas(t[1])

def p_registro_acceso(t):
    '''registro :   acceso'''
    t[0]=t[1]
                
def p_acceso(t):
    '''acceso   :   variable dimension
                |   variable'''
    t[0]=ExpresionVariable(t[1])

def p_dimension(t):
    '''dimension    :   dimension CORCHETEIZQ inside CORCHETEDER 
                    |   CORCHETEIZQ inside CORCHETEDER
                '''
    t[0]=t[1]

def p_inside(t):
    '''inside   :   ENTERO
                |   CADENA
                |   acceso'''
    t[0]=t[1]


def p_conversion(t):
    'conversion   : PARIZQ eltipo PARDER registro'
    t[0]=t[1]

def p_eltipo(t):
    '''eltipo   :   FLOAT
                |   INT
                |   CHAR'''
# ====================== Gramatica Para las Palabras Reservadas y funciones especiales
def p_exit(t):
    'exit   :   EXIT PTCOMA'
    t[0]=t[1]
def p_print(t):
    'print  : PRINT PARIZQ instruccionregistro PARDER PTCOMA'
    t[0]=Imprimir('Javier')
def p_etiqueta(t):
    'etiqueta   :  ETIQUETA DOSPUNTOS' #
    t[0]=t[1] 
def p_goto(t):
    'goto   :   GOTO ETIQUETA PTCOMA' #
    t[0]=t[1]
def p_read(t):
    'read   :   READ PARIZQ PARDER PTCOMA'
    t[0]=t[1]
def p_unset(t):
    'unset  :   UNSET PARIZQ registro PARDER PTCOMA'
    t[0]=t[1]
def p_if(t):
    'ifcomando :    IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA'
    t[0]=t[1]



def p_error(t):
    if not t:
        print("EOF")
        return
   
    linea =find_column(entrada,t)
    t.lexpos=linea
    print(t)
    print("Error sintáctico en '%s'" % t.value)
     # Buscando el proximo token tipo ;
    while True:
        tok = parser.token()
           # busca el siguiente token
        if not tok or tok.type == "PTCOMA": 
            break
    parser.errok() # quita los tokens y retorna el token de  recuperacion
    return tok

parser = yacc.yacc()



# Funcion que corre nuestro parse
def parse(input) :
    global entrada
    entrada=input
    return parser.parse(input)
