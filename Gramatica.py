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

def p_lista_instrucciones(t):
    'listainstrucciones :   listainstrucciones simpleinstrucciones'

def p_lista_instrucciones_simple(t):
    'listainstrucciones : simpleinstrucciones'
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
def p_declaracion(t):
    'declaracion   :    variable PTCOMA'
def p_asignacion(t):
    'asignacion :   variable IGUAL tipo PTCOMA'
def p_tipo(t):
    '''tipo :   instruccionregistro
            |   conversion
            |   ARRAY PARIZQ PARDER'''
def p_variable(t):
    '''variable :   TEMPORALES
                |   PARAMETROS
                |   DEVOLUCIONES
                |   RETORNONIVEL
                |   PILA
                |   SP'''
def p_instruccionregistro(t):        
    '''instruccionregistro  : registro MAS registro
                            | registro MENOS registro 
                            | registro POR registro 
                            | registro DIVIDIDO registro 
                            | registro RESIDUO registro 
                            | ABS PARIZQ registro PARDER 
                            | registro ANDLOGICA registro
                            | registro ORLOGICA registro 
                            | registro XOR registro 
                            | NOTLOGICA registro
                            | registro ANDBIT registro
                            | registro ORBIT registro 
                            | registro XORBIT registro 
                            | registro SHIFTIZQ registro 
                            | registro SHIFTDER registro 
                            | NOTBIT registro
                            | registro IGUALIGUAL registro
                            | registro NOIGUAL registro 
                            | registro MAYORIGUAL registro 
                            | registro MENORIGUAL registro 
                            | registro MAYOR registro 
                            | registro MENOR registro
                            | MENOS registro %prec UMENOS 
                            | registro'''
def p_registro(t):
    '''registro :   acceso
                |   ENTERO
                |   CADENA
                |   DECIMAL'''
def p_acceso(t):
    '''acceso   :   variable dimension
                |   variable'''
def p_dimension(t):
    '''dimension    :   dimension CORCHETEIZQ inside CORCHETEDER 
                    |   CORCHETEIZQ inside CORCHETEDER
                '''
def p_inside(t):
    '''inside   :   ENTERO
                |   CADENA
                |   acceso'''


def p_conversion(t):
    'conversion   : PARIZQ eltipo PARDER registro'

def p_eltipo(t):
    '''eltipo   :   FLOAT
                |   INT
                |   CHAR'''
# ====================== Gramatica Para las Palabras Reservadas y funciones especiales
def p_exit(t):
    'exit   :   EXIT PTCOMA'
def p_print(t):
    'print  : PRINT PARIZQ instruccionregistro PARDER PTCOMA'
def p_etiqueta(t):
    'etiqueta   :  ETIQUETA DOSPUNTOS' # 
def p_goto(t):
    'goto   :   GOTO ETIQUETA PTCOMA' #
def p_read(t):
    'read   :   READ PARIZQ PARDER PTCOMA'
def p_unset(t):
    'unset  :   UNSET PARIZQ registro PARDER PTCOMA'
def p_if(t):
    'ifcomando :    IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA'



def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    if not t:
         print("End of File!")
         return
 
     # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()
           # Get the next token
        if not tok or tok.type == "PTCOMA": 
            break
    parser.errok()
    return tok

parser = yacc.yacc()



# Funcion que corre nuestro parse
def parse(input) :
    return parser.parse(input)
f = open("./entrada.txt", "r")
input = f.read()
parse(input)        