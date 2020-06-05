from enum import Enum

class TIPO_DATO(Enum) :
    NUMERO = 1
    CADENA=2
    FLOAT=3
    METODO=4
    FUNCION=5
    
class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, valor) :
        self.id = id
        self.tipo = tipo
        self.valor = valor # para etiqueta valor sera mi posicion

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos[simbolo.id] = simbolo
    
    def obtener(self, id) :
        if not id in self.simbolos :
            #print('Error: variable ', id, ' no definida.')
            return None # ya se puede asignar o crear

        return self.simbolos[id]

    def actualizar(self, simbolo) :
        if not simbolo.id in self.simbolos :
            print('Error: variable ', simbolo.id, ' no definida.')
        else :
            self.simbolos[simbolo.id] = simbolo

    def EliminarSimbolo(self,id):
        self.simbolos.pop(id)

    def ObtenerTabla(self):
        return self.simbolos