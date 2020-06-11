class Error:
    ''' Representa los valores de los errores encontrados'''
    def __init__(self,tipo,lexema,descripcion,linea,columna):
        self.tipo=tipo
        self.lexema=lexema
        self.descripcion=descripcion
        self.linea=linea
        self.columna=columna

class ListaError:
    def __init__(self,lista=[]):
        self.lista=lista

    def AddError(self,error):
        self.lista.append(error)
        
    def ObtenerLista(self):
        return self.lista


