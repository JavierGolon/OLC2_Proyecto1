class Instruccion:
    ''' Representa la clase padre de las instrucciones'''
#======================= CLASES QUE HEREDAN DE LA CLASE INSTRUCCION ===============
class declaracion(Instruccion):
    def __init__(self,variable):
        self.variable=variable

class asignacion(Instruccion):
    def __init__(self,variable,valor):
        self.variable=variable
        self.valor=valor

class instruccionIf(Instruccion):
    def __init__(self,exprelogica,goto):
        self.exprelogica=exprelogica
        self.goto=goto

class Exit(Instruccion):
    def __init__(self,iden):
        self.iden=iden

class Imprimir(Instruccion):
    def __init__(self,cadena):
        self.cadena=cadena

class Etiqueta(Instruccion):
    def __init__(self,iden):
        self.iden=iden

class Goto(Instruccion):
    def __init__(self,label):
        self.label=label

class Read(Instruccion):
    def __init__(self,valor):
        self.valor=valor

class Unset(Instruccion):
    def __init__(self,registro):
        self.registro=registro

# clases de expresiones de asignacion especiales

class Casteo(Instruccion):
    def __init__(self,tipo,valor):
        self.tipo=tipo
        self.valor=valor
class Arreglo(Instruccion):
    def __init__(self,registro,dimension):
        self.registro=registro
        self.dimension=dimension
        