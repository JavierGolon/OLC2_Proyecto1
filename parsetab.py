
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftXORleftORLOGICAleftANDLOGICAleftORBITleftXORBITleftANDBITleftNOTBITnonassocMAYORMENORMAYORIGUALMENORIGUALNOIGUALIGUALIGUALleftSHIFTIZQSHIFTDERleftMASMENOSleftPORDIVIDIDORESIDUOrightNOTLOGICArightUMENOSABS ANDBIT ANDLOGICA ARRAY CADENA CHAR CORCHETEDER CORCHETEIZQ DECIMAL DEVOLUCIONES DIVIDIDO DOSPUNTOS ENTERO ETIQUETA EXIT FLOAT GOTO IF IGUAL IGUALIGUAL INT MAIN MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS NOIGUAL NOTBIT NOTLOGICA ORBIT ORLOGICA PARAMETROS PARDER PARIZQ PILA POR PRINT PTCOMA READ RESIDUO RETORNONIVEL SHIFTDER SHIFTIZQ SP TEMPORALES UNSET XOR XORBITinit  :    MAIN DOSPUNTOS listainstruccioneslistainstrucciones :   listainstrucciones simpleinstruccioneslistainstrucciones : simpleinstruccionessimpleinstrucciones    : declaracion\n                              | asignacion\n                              | ifcomando\n                              | exit\n                              | print\n                              | etiqueta\n                              | goto\n                              | read\n                              | unsetdeclaracion   :    variable PTCOMAasignacion :   variable IGUAL tipo PTCOMAtipo :   instruccionregistro\n            |   conversion\n            |   arreglovariable :   TEMPORALES\n                |   PARAMETROS\n                |   DEVOLUCIONES\n                |   RETORNONIVEL\n                |   PILA\n                |   SPinstruccionregistro  : registro MAS registro\n                            | registro MENOS registro \n                            | registro POR registro \n                            | registro DIVIDIDO registro \n                            | registro RESIDUO registro \n                            | registro ANDLOGICA registro\n                            | registro ORLOGICA registro \n                            | registro XOR registro \n                            | registro ANDBIT registro\n                            | registro ORBIT registro \n                            | registro XORBIT registro \n                            | registro SHIFTIZQ registro \n                            | registro SHIFTDER registro \n                            | registro IGUALIGUAL registro\n                            | registro NOIGUAL registro \n                            | registro MAYORIGUAL registro \n                            | registro MENORIGUAL registro \n                            | registro MAYOR registro \n                            | registro MENOR registroinstruccionregistro  : registroregistro  : ABS PARIZQ registro PARDER \n                            | NOTLOGICA registro \n                            | NOTBIT registro\n                            | MENOS registro %prec UMENOS\n                            | ANDBIT registroregistro :   ENTERO\n                |   DECIMALregistro :   CADENAregistro :   accesoacceso   :   variable dimension\n                |   variabledimension    :   dimension CORCHETEIZQ inside CORCHETEDER \n                    |   CORCHETEIZQ inside CORCHETEDER\n                inside   :   ENTERO\n                |   CADENA\n                |   accesoconversion   : PARIZQ eltipo PARDER registroarreglo    :   ARRAY PARIZQ PARDEReltipo   :   FLOAT\n                |   INT\n                |   CHARexit   :   EXIT PTCOMAprint  : PRINT PARIZQ registro PARDER PTCOMAetiqueta   :  ETIQUETA DOSPUNTOSgoto   :   GOTO ETIQUETA PTCOMAread   :   READ PARIZQ PARDER PTCOMAunset  :   UNSET PARIZQ acceso PARDER PTCOMAifcomando :    IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA'
    
_lr_action_items = {'MAIN':([0,],[2,]),'$end':([1,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,95,125,126,133,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,-69,-66,-70,-71,]),'DOSPUNTOS':([2,18,],[3,34,]),'IF':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,95,125,126,133,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,-69,-66,-70,-71,]),'EXIT':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,95,125,126,133,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,-69,-66,-70,-71,]),'PRINT':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,95,125,126,133,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,-69,-66,-70,-71,]),'ETIQUETA':([3,4,5,6,7,8,9,10,11,12,13,14,17,29,30,34,35,57,63,95,124,125,126,133,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,33,-2,-13,-67,-65,-68,-14,-69,131,-66,-70,-71,]),'GOTO':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,93,95,125,126,133,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,124,-69,-66,-70,-71,]),'READ':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,95,125,126,133,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,-69,-66,-70,-71,]),'UNSET':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,57,63,95,125,126,133,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-67,-65,-68,-14,-69,-66,-70,-71,]),'TEMPORALES':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,45,46,50,51,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,95,97,121,125,126,133,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,23,23,-67,-65,23,23,23,23,23,23,-68,23,-14,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-69,23,23,-66,-70,-71,]),'PARAMETROS':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,45,46,50,51,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,95,97,121,125,126,133,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,24,24,-67,-65,24,24,24,24,24,24,-68,24,-14,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-69,24,24,-66,-70,-71,]),'DEVOLUCIONES':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,45,46,50,51,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,95,97,121,125,126,133,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,25,25,-67,-65,25,25,25,25,25,25,-68,25,-14,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-69,25,25,-66,-70,-71,]),'RETORNONIVEL':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,45,46,50,51,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,95,97,121,125,126,133,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,26,26,-67,-65,26,26,26,26,26,26,-68,26,-14,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-69,26,26,-66,-70,-71,]),'PILA':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,45,46,50,51,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,95,97,121,125,126,133,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,27,27,-67,-65,27,27,27,27,27,27,-68,27,-14,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-69,27,27,-66,-70,-71,]),'SP':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,45,46,50,51,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,95,97,121,125,126,133,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,28,28,-67,-65,28,28,28,28,28,28,-68,28,-14,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-69,28,28,-66,-70,-71,]),'PTCOMA':([15,19,23,24,25,26,27,28,33,39,40,41,42,43,44,52,53,54,55,59,61,83,84,91,92,94,96,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,128,129,130,131,132,],[30,35,-18,-19,-20,-21,-22,-23,57,-54,63,-15,-16,-17,-43,-49,-50,-51,-52,95,-53,-47,-48,-45,-46,125,126,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-61,-56,-60,-44,133,-55,]),'IGUAL':([15,23,24,25,26,27,28,],[31,-18,-19,-20,-21,-22,-23,]),'PARIZQ':([16,20,21,22,31,48,49,],[32,36,37,38,47,89,90,]),'CORCHETEIZQ':([23,24,25,26,27,28,39,61,128,132,],[-18,-19,-20,-21,-22,-23,62,97,-56,-55,]),'MAS':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,64,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'MENOS':([23,24,25,26,27,28,31,32,36,39,44,45,46,50,51,52,53,54,55,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,90,91,92,121,128,130,132,],[-18,-19,-20,-21,-22,-23,45,45,45,-54,65,45,45,45,45,-49,-50,-51,-52,-53,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-47,-48,45,-45,-46,45,-56,-44,-55,]),'POR':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,66,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'DIVIDIDO':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,67,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'RESIDUO':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,68,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'ANDLOGICA':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,69,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'ORLOGICA':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,70,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'XOR':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,71,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'ANDBIT':([23,24,25,26,27,28,31,32,36,39,44,45,46,50,51,52,53,54,55,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,90,91,92,121,128,130,132,],[-18,-19,-20,-21,-22,-23,46,46,46,-54,72,46,46,46,46,-49,-50,-51,-52,-53,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-47,-48,46,-45,-46,46,-56,-44,-55,]),'ORBIT':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,73,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'XORBIT':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,74,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'SHIFTIZQ':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,75,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'SHIFTDER':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,76,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'IGUALIGUAL':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,77,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'NOIGUAL':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,78,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'MAYORIGUAL':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,79,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'MENORIGUAL':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,80,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'MAYOR':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,81,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'MENOR':([23,24,25,26,27,28,39,44,52,53,54,55,61,83,84,91,92,128,130,132,],[-18,-19,-20,-21,-22,-23,-54,82,-49,-50,-51,-52,-53,-47,-48,-45,-46,-56,-44,-55,]),'PARDER':([23,24,25,26,27,28,37,39,44,52,53,54,55,56,58,60,61,83,84,85,86,87,88,89,91,92,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,128,130,132,],[-18,-19,-20,-21,-22,-23,59,-54,-43,-49,-50,-51,-52,93,94,96,-53,-47,-48,121,-62,-63,-64,122,-45,-46,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,130,-56,-44,-55,]),'CORCHETEDER':([23,24,25,26,27,28,39,61,98,99,100,101,127,128,132,],[-18,-19,-20,-21,-22,-23,-54,-53,128,-57,-58,-59,132,-56,-55,]),'ARRAY':([31,],[48,]),'ABS':([31,32,36,45,46,50,51,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,121,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'NOTLOGICA':([31,32,36,45,46,50,51,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,121,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'NOTBIT':([31,32,36,45,46,50,51,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,121,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'ENTERO':([31,32,36,45,46,50,51,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,97,121,],[52,52,52,52,52,52,52,99,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,99,52,]),'DECIMAL':([31,32,36,45,46,50,51,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,121,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'CADENA':([31,32,36,45,46,50,51,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,97,121,],[54,54,54,54,54,54,54,100,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,100,54,]),'FLOAT':([47,],[86,]),'INT':([47,],[87,]),'CHAR':([47,],[88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'listainstrucciones':([3,],[4,]),'simpleinstrucciones':([3,4,],[5,29,]),'declaracion':([3,4,],[6,6,]),'asignacion':([3,4,],[7,7,]),'ifcomando':([3,4,],[8,8,]),'exit':([3,4,],[9,9,]),'print':([3,4,],[10,10,]),'etiqueta':([3,4,],[11,11,]),'goto':([3,4,],[12,12,]),'read':([3,4,],[13,13,]),'unset':([3,4,],[14,14,]),'variable':([3,4,31,32,36,38,45,46,50,51,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,97,121,],[15,15,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'tipo':([31,],[40,]),'instruccionregistro':([31,32,],[41,56,]),'conversion':([31,],[42,]),'arreglo':([31,],[43,]),'registro':([31,32,36,45,46,50,51,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,121,],[44,44,58,83,84,91,92,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,123,129,]),'acceso':([31,32,36,38,45,46,50,51,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,97,121,],[55,55,55,60,55,55,55,55,101,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,101,55,]),'dimension':([39,],[61,]),'eltipo':([47,],[85,]),'inside':([62,97,],[98,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> MAIN DOSPUNTOS listainstrucciones','init',3,'p_init','Gramatica.py',207),
  ('listainstrucciones -> listainstrucciones simpleinstrucciones','listainstrucciones',2,'p_lista_instrucciones','Gramatica.py',211),
  ('listainstrucciones -> simpleinstrucciones','listainstrucciones',1,'p_lista_instrucciones_simple','Gramatica.py',216),
  ('simpleinstrucciones -> declaracion','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',219),
  ('simpleinstrucciones -> asignacion','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',220),
  ('simpleinstrucciones -> ifcomando','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',221),
  ('simpleinstrucciones -> exit','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',222),
  ('simpleinstrucciones -> print','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',223),
  ('simpleinstrucciones -> etiqueta','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',224),
  ('simpleinstrucciones -> goto','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',225),
  ('simpleinstrucciones -> read','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',226),
  ('simpleinstrucciones -> unset','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',227),
  ('declaracion -> variable PTCOMA','declaracion',2,'p_declaracion','Gramatica.py',230),
  ('asignacion -> variable IGUAL tipo PTCOMA','asignacion',4,'p_asignacion','Gramatica.py',233),
  ('tipo -> instruccionregistro','tipo',1,'p_tipo','Gramatica.py',236),
  ('tipo -> conversion','tipo',1,'p_tipo','Gramatica.py',237),
  ('tipo -> arreglo','tipo',1,'p_tipo','Gramatica.py',238),
  ('variable -> TEMPORALES','variable',1,'p_variable','Gramatica.py',241),
  ('variable -> PARAMETROS','variable',1,'p_variable','Gramatica.py',242),
  ('variable -> DEVOLUCIONES','variable',1,'p_variable','Gramatica.py',243),
  ('variable -> RETORNONIVEL','variable',1,'p_variable','Gramatica.py',244),
  ('variable -> PILA','variable',1,'p_variable','Gramatica.py',245),
  ('variable -> SP','variable',1,'p_variable','Gramatica.py',246),
  ('instruccionregistro -> registro MAS registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',249),
  ('instruccionregistro -> registro MENOS registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',250),
  ('instruccionregistro -> registro POR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',251),
  ('instruccionregistro -> registro DIVIDIDO registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',252),
  ('instruccionregistro -> registro RESIDUO registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',253),
  ('instruccionregistro -> registro ANDLOGICA registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',254),
  ('instruccionregistro -> registro ORLOGICA registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',255),
  ('instruccionregistro -> registro XOR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',256),
  ('instruccionregistro -> registro ANDBIT registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',257),
  ('instruccionregistro -> registro ORBIT registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',258),
  ('instruccionregistro -> registro XORBIT registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',259),
  ('instruccionregistro -> registro SHIFTIZQ registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',260),
  ('instruccionregistro -> registro SHIFTDER registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',261),
  ('instruccionregistro -> registro IGUALIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',262),
  ('instruccionregistro -> registro NOIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',263),
  ('instruccionregistro -> registro MAYORIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',264),
  ('instruccionregistro -> registro MENORIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',265),
  ('instruccionregistro -> registro MAYOR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',266),
  ('instruccionregistro -> registro MENOR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',267),
  ('instruccionregistro -> registro','instruccionregistro',1,'p_instruccion_registrounico','Gramatica.py',290),
  ('registro -> ABS PARIZQ registro PARDER','registro',4,'p_instruccionregistro_diferentes','Gramatica.py',294),
  ('registro -> NOTLOGICA registro','registro',2,'p_instruccionregistro_diferentes','Gramatica.py',295),
  ('registro -> NOTBIT registro','registro',2,'p_instruccionregistro_diferentes','Gramatica.py',296),
  ('registro -> MENOS registro','registro',2,'p_instruccionregistro_diferentes','Gramatica.py',297),
  ('registro -> ANDBIT registro','registro',2,'p_instruccionregistro_diferentes','Gramatica.py',298),
  ('registro -> ENTERO','registro',1,'p_registro','Gramatica.py',306),
  ('registro -> DECIMAL','registro',1,'p_registro','Gramatica.py',307),
  ('registro -> CADENA','registro',1,'p_registro_cadena','Gramatica.py',311),
  ('registro -> acceso','registro',1,'p_registro_acceso','Gramatica.py',315),
  ('acceso -> variable dimension','acceso',2,'p_acceso','Gramatica.py',319),
  ('acceso -> variable','acceso',1,'p_acceso','Gramatica.py',320),
  ('dimension -> dimension CORCHETEIZQ inside CORCHETEDER','dimension',4,'p_dimension','Gramatica.py',324),
  ('dimension -> CORCHETEIZQ inside CORCHETEDER','dimension',3,'p_dimension','Gramatica.py',325),
  ('inside -> ENTERO','inside',1,'p_inside','Gramatica.py',330),
  ('inside -> CADENA','inside',1,'p_inside','Gramatica.py',331),
  ('inside -> acceso','inside',1,'p_inside','Gramatica.py',332),
  ('conversion -> PARIZQ eltipo PARDER registro','conversion',4,'p_conversion','Gramatica.py',337),
  ('arreglo -> ARRAY PARIZQ PARDER','arreglo',3,'p_arreglo','Gramatica.py',340),
  ('eltipo -> FLOAT','eltipo',1,'p_eltipo','Gramatica.py',344),
  ('eltipo -> INT','eltipo',1,'p_eltipo','Gramatica.py',345),
  ('eltipo -> CHAR','eltipo',1,'p_eltipo','Gramatica.py',346),
  ('exit -> EXIT PTCOMA','exit',2,'p_exit','Gramatica.py',350),
  ('print -> PRINT PARIZQ registro PARDER PTCOMA','print',5,'p_print','Gramatica.py',353),
  ('etiqueta -> ETIQUETA DOSPUNTOS','etiqueta',2,'p_etiqueta','Gramatica.py',356),
  ('goto -> GOTO ETIQUETA PTCOMA','goto',3,'p_goto','Gramatica.py',359),
  ('read -> READ PARIZQ PARDER PTCOMA','read',4,'p_read','Gramatica.py',362),
  ('unset -> UNSET PARIZQ acceso PARDER PTCOMA','unset',5,'p_unset','Gramatica.py',365),
  ('ifcomando -> IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA','ifcomando',7,'p_if','Gramatica.py',368),
]
