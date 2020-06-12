from graphviz import Digraph
from Expresiones import *
from Instrucciones import *
dot = Digraph(format='jpg')



class Graficadora:
    def __init__(self):
        self.indice = 0

    def Recorrer_Instrucciones_Inicio(self, instrucciones):

        dot.node('A', 'Main')
        for inst in instrucciones:
            if isinstance(inst, Imprimir):
                dot.node(str(self.New_Indice()), 'Imprimir')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_imprimir(inst,str(self.Actual_Indice()))
            elif isinstance(inst, asignacion):
                dot.node(str(self.New_Indice()), 'Asignar')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_asignar(inst,str(self.Actual_Indice()))
            elif isinstance(inst, declaracion):
                dot.node(str(self.New_Indice()), 'Declarar')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_declarar(inst,str(self.Actual_Indice()))
            elif isinstance(inst, Unset):
                dot.node(str(self.New_Indice()), 'Unset')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_Unset(inst.registro,str(self.Actual_Indice()))
            elif isinstance(inst, instruccionIf):
                dot.node(str(self.New_Indice()), 'If')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_if(inst,str(self.Actual_Indice()))
            elif isinstance(inst, Goto):
                dot.node(str(self.New_Indice()), 'Goto')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_goto(inst,str(self.Actual_Indice()))
            elif isinstance(inst, Exit):
                dot.node(str(self.New_Indice()), 'Exit')
                dot.edge('A', str(self.Actual_Indice()))
                ''' No tiene Hijos '''
            elif isinstance(inst, Etiqueta):
                dot.node(str(self.New_Indice()), 'Etiqueta')
                dot.edge('A', str(self.Actual_Indice()))
                self.Recorre_Etiqueta(inst,str(self.Actual_Indice()))

        dot.render('Img_Reportes/AST.gv')
        'Img_Reportest/AST.gv.jpg'

    def New_Indice(self):
        self.indice += 1
        return self.indice

    def Actual_Indice(self):
        return self.indice


    def Recorre_Etiqueta(self, inst, padre):
        ''' instruccion con hijo '''
        dot.node(str(self.New_Indice()), inst.iden)
        dot.edge(padre, str(self.Actual_Indice()))

    def Recorre_goto(self, inst, padre):
        dot.node(str(self.New_Indice()), inst.label)
        dot.edge(padre, str(self.Actual_Indice()))
        pass

    def Recorre_if(self, inst, padre):
        dot.node(str(self.New_Indice()),'Expresion')
        dot.edge(padre, str(self.Actual_Indice()))
        padre1 = str(self.Actual_Indice())
        self.resolver_Expresion(inst.exprelogica,padre1)
        dot.node(str(self.New_Indice()),'Goto')
        dot.edge(padre, str(self.Actual_Indice()))
        padre2 = str(self.Actual_Indice())
        dot.node(str(self.New_Indice()),str(inst.goto))
        dot.edge(padre2, str(self.Actual_Indice()))

    def Recorre_read(self, inst, padre):
        pass

    def Recorre_Unset(self, inst, padre):
        dot.node(str(self.New_Indice()),str(inst.registro))
        dot.edge(padre, str(self.Actual_Indice()))
        

    def Recorre_asignar(self, inst, padre):
        if isinstance(inst.valor,ExpresionReferencia):
            
            dot.node(str(self.New_Indice()),'=')
            dot.edge(padre, str(self.Actual_Indice()))
            padre1 = str(self.Actual_Indice())
            dot.node(str(self.New_Indice()),inst.variable.registro)
            dot.edge(padre1, str(self.Actual_Indice()))
            dot.node(str(self.New_Indice()),'&')
            dot.edge(padre1, str(self.Actual_Indice()))
            padre2 = str(self.Actual_Indice())
            self.resolver_Expresion(inst.valor.registro,padre2) 
        elif isinstance(inst.variable,ExpresionArreglo):
            dot.node(str(self.New_Indice()),'=')
            dot.edge(padre, str(self.Actual_Indice()))
            padre1 = str(self.Actual_Indice())
            dot.node(str(self.New_Indice()),inst.variable.id)
            dot.edge(padre1, str(self.Actual_Indice()))
            padre2 = str(self.Actual_Indice()) 
            for lista in inst.variable.dimension:
                dot.node(str(self.New_Indice()),'[]')
                dot.edge(padre2, str(self.Actual_Indice()))
                self.resolver_Expresion(lista.registro,str(self.Actual_Indice()))
            
            self.resolver_Expresion(inst.valor,padre1)
        else:
            dot.node(str(self.New_Indice()),'=')
            dot.edge(padre, str(self.Actual_Indice()))
            padre1 = str(self.Actual_Indice())
            dot.node(str(self.New_Indice()),inst.variable.registro)
            dot.edge(padre1, str(self.Actual_Indice())) 
            self.resolver_Expresion(inst.valor,padre1)

    def Recorre_declarar(self, inst, padre):
        dot.node(str(self.New_Indice()),str(inst.variable))
        dot.edge(padre, str(self.Actual_Indice()))

    def Recorre_imprimir(self, inst, padre):
        self.resolver_Expresion(inst.cadena,padre)

    def resolver_Expresion(self, Expresion,padre):
        if isinstance(Expresion,ExpresionBinariaAritmetica):
            if Expresion.operador == OPERACION_ARITMETICA.MAS :
                dot.node(str(self.New_Indice()),'+')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
            elif Expresion.operador == OPERACION_ARITMETICA.MENOS:
                dot.node(str(self.New_Indice()),'-')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif Expresion.operador == OPERACION_ARITMETICA.POR:
                dot.node(str(self.New_Indice()),'*')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif Expresion.operador == OPERACION_ARITMETICA.DIVIDIDO:
                dot.node(str(self.New_Indice()),'/')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif Expresion.operador == OPERACION_ARITMETICA.RESIDUO:
                dot.node(str(self.New_Indice()),'%')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
               
        elif isinstance(Expresion,ExpresionBinariaRelacional):
            if Expresion.operador == OPEREACION_RELACIONAL.IGUAL :
                dot.node(str(self.New_Indice()),'==')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
               
            if Expresion.operador == OPEREACION_RELACIONAL.DIFERENTE :
                dot.node(str(self.New_Indice()),'!=')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
              
            if Expresion.operador == OPEREACION_RELACIONAL.MAYORIGUAL :
                dot.node(str(self.New_Indice()),'>=')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
               
            if Expresion.operador == OPEREACION_RELACIONAL.MENORIGUAL :
                dot.node(str(self.New_Indice()),'<=')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            if Expresion.operador == OPEREACION_RELACIONAL.MAYOR :
                dot.node(str(self.New_Indice()),'>')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
              
            if Expresion.operador == OPEREACION_RELACIONAL.MENOR :
                dot.node(str(self.New_Indice()),'<')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
            
        elif isinstance(Expresion,ExpresionBinarioLogica):
            if Expresion.operador == OPERACION_LOGICA.AND :
                dot.node(str(self.New_Indice()),'&&')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif Expresion.operador == OPERACION_LOGICA.OR :
                dot.node(str(self.New_Indice()),'||')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif Expresion.operador == OPERACION_LOGICA.XOR :
                dot.node(str(self.New_Indice()),'xor')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
            
        elif isinstance(Expresion,ExpresionBinariaBit):
            if(Expresion.operador ==OPERACION_BIT.AND):
                dot.node(str(self.New_Indice()),'&')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif(Expresion.operador ==OPERACION_BIT.OR):
                dot.node(str(self.New_Indice()),'|')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
               
            elif(Expresion.operador ==OPERACION_BIT.XOR):
                dot.node(str(self.New_Indice()),'^')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
               
            elif(Expresion.operador ==OPERACION_BIT.SHIFTIZQ):
                dot.node(str(self.New_Indice()),'<<')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
                
            elif(Expresion.operador ==OPERACION_BIT.SHIFTDER):
                dot.node(str(self.New_Indice()),'>>')
                dot.edge(padre, str(self.Actual_Indice()))
                padre1 = self.Actual_Indice()
                self.resolver_Expresion(Expresion.exp1,str(padre1))
                self.resolver_Expresion(Expresion.exp2,str(padre1))
        elif isinstance(Expresion,ExpresionMonoLogica):
            dot.node(str(self.New_Indice()),'!')
            dot.edge(padre, str(self.Actual_Indice()))
            self.resolver_Expresion(Expresion.exp,str(self.Actual_Indice()))
                
        elif isinstance(Expresion,ExpresionMonoBit):
            dot.node(str(self.New_Indice()),'~')
            dot.edge(padre, str(self.Actual_Indice()))
            self.resolver_Expresion(Expresion.exp,str(self.Actual_Indice()))   
        elif isinstance(Expresion,ExpresionNumero):
            dot.node(str(self.New_Indice()),str(Expresion.valor))
            dot.edge(padre, str(self.Actual_Indice()))

        elif isinstance(Expresion,ExpresionComillas):
            dot.node(str(self.New_Indice()),Expresion.valor)
            dot.edge(padre, str(self.Actual_Indice()))
        elif isinstance(Expresion,ExpresionNegativo):
            dot.node(str(self.New_Indice()),'-')
            dot.edge(padre, str(self.Actual_Indice()))
            self.resolver_Expresion(Expresion.exp,str(self.Actual_Indice()))
        elif isinstance(Expresion,ExpresionAbs):
            dot.node(str(self.New_Indice()),'-')
            dot.edge(padre, str(self.Actual_Indice()))
            self.resolver_Expresion(Expresion.exp,str(self.Actual_Indice()))
        elif isinstance(Expresion,ExpresionVariable):
            dot.node(str(self.New_Indice()),str(Expresion.registro))
            dot.edge(padre, str(self.Actual_Indice()))
        elif isinstance(Expresion,Arreglo):
            pass
        elif isinstance(Expresion,Casteo):
            dot.node(str(self.New_Indice()),'Casteo')
            dot.edge(padre, str(self.Actual_Indice()))
            padre1 = str(self.Actual_Indice())
            dot.node(str(self.New_Indice()),str(Expresion.tipo))
            dot.edge(padre1, str(self.Actual_Indice()))
            self.resolver_Expresion(Expresion.valor,padre1)
        elif isinstance(Expresion,Read):
            dot.node(str(self.New_Indice()),'Read()')
            dot.edge(padre, str(self.Actual_Indice()))
        elif isinstance(Expresion,ExpresionArreglo):
            dot.node(str(self.New_Indice()),Expresion.id)
            dot.edge(padre, str(self.Actual_Indice()))
            padre1 = str(self.Actual_Indice()) 
            for lista in Expresion.dimension:
                dot.node(str(self.New_Indice()),'[]')
                dot.edge(padre1, str(self.Actual_Indice()))
                self.resolver_Expresion(lista.registro,str(self.Actual_Indice()))




        




