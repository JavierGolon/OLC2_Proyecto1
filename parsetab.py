
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftXORleftORLOGICAleftANDLOGICAleftORBITleftXORBITleftANDBITleftNOTBITnonassocMAYORMENORMAYORIGUALMENORIGUALNOIGUALIGUALIGUALleftSHIFTIZQSHIFTDERleftMASMENOSleftPORDIVIDIDORESIDUOrightNOTLOGICArightUMENOSABS ANDBIT ANDLOGICA ARRAY CADENA CHAR CORCHETEDER CORCHETEIZQ DECIMAL DEVOLUCIONES DIVIDIDO DOSPUNTOS ENTERO ETIQUETA EXIT FLOAT GOTO IF IGUAL IGUALIGUAL INT MAIN MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS NOIGUAL NOTBIT NOTLOGICA ORBIT ORLOGICA PARAMETROS PARDER PARIZQ PILA POR PRINT PTCOMA READ RESIDUO RETORNONIVEL SHIFTDER SHIFTIZQ SP TEMPORALES UNSET XOR XORBITinit  :    MAIN DOSPUNTOS listainstruccioneslistainstrucciones :   listainstrucciones simpleinstruccioneslistainstrucciones : simpleinstruccionessimpleinstrucciones    : declaracion\n                              | asignacion\n                              | ifcomando\n                              | exit\n                              | print\n                              | etiqueta\n                              | goto\n                              | read\n                              | unsetdeclaracion   :    variable PTCOMAasignacion :   variable IGUAL tipo PTCOMAtipo :   instruccionregistro\n            |   conversion\n            |   ARRAY PARIZQ PARDERvariable :   TEMPORALES\n                |   PARAMETROS\n                |   DEVOLUCIONES\n                |   RETORNONIVEL\n                |   PILA\n                |   SPinstruccionregistro  : registro MAS registro\n                            | registro MENOS registro \n                            | registro POR registro \n                            | registro DIVIDIDO registro \n                            | registro RESIDUO registro \n                            | ABS PARIZQ registro PARDER \n                            | registro ANDLOGICA registro\n                            | registro ORLOGICA registro \n                            | registro XOR registro \n                            | NOTLOGICA registro\n                            | registro ANDBIT registro\n                            | registro ORBIT registro \n                            | registro XORBIT registro \n                            | registro SHIFTIZQ registro \n                            | registro SHIFTDER registro \n                            | NOTBIT registro\n                            | registro IGUALIGUAL registro\n                            | registro NOIGUAL registro \n                            | registro MAYORIGUAL registro \n                            | registro MENORIGUAL registro \n                            | registro MAYOR registro \n                            | registro MENOR registro\n                            | MENOS registro %prec UMENOS \n                            | registroregistro :   acceso\n                |   ENTERO\n                |   CADENA\n                |   DECIMALacceso   :   variable dimension\n                |   variabledimension    :   dimension CORCHETEIZQ inside CORCHETEDER \n                    |   CORCHETEIZQ inside CORCHETEDER\n                inside   :   ENTERO\n                |   CADENA\n                |   accesoconversion   : PARIZQ eltipo PARDER registroeltipo   :   FLOAT\n                |   INT\n                |   CHARexit   :   EXIT PTCOMAprint  : PRINT PARIZQ instruccionregistro PARDER PTCOMAetiqueta   :  ETIQUETA DOSPUNTOSgoto   :   GOTO ETIQUETA PTCOMAread   :   READ PARIZQ PARDER PTCOMAunset  :   UNSET PARIZQ registro PARDER PTCOMAifcomando :    IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA'
    
_lr_action_items = {'MAIN':([0,],[2,]),'$end':([1,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,92,122,123,130,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,-67,-64,-68,-69,]),'DOSPUNTOS':([2,18,],[3,34,]),'IF':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,92,122,123,130,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,-67,-64,-68,-69,]),'EXIT':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,92,122,123,130,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,-67,-64,-68,-69,]),'PRINT':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,92,122,123,130,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,-67,-64,-68,-69,]),'ETIQUETA':([3,4,5,6,7,8,9,10,11,12,13,14,17,29,30,34,35,55,61,92,121,122,123,130,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,33,-2,-13,-65,-63,-66,-14,-67,128,-64,-68,-69,]),'GOTO':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,90,92,122,123,130,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,121,-67,-64,-68,-69,]),'READ':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,92,122,123,130,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,-67,-64,-68,-69,]),'UNSET':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,34,35,55,61,92,122,123,130,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,-65,-63,-66,-14,-67,-64,-68,-69,]),'TEMPORALES':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,46,48,49,55,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,92,94,100,122,123,130,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,23,23,-65,-63,23,23,23,23,23,-66,23,-14,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-67,23,23,-64,-68,-69,]),'PARAMETROS':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,46,48,49,55,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,92,94,100,122,123,130,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,24,24,-65,-63,24,24,24,24,24,-66,24,-14,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-67,24,24,-64,-68,-69,]),'DEVOLUCIONES':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,46,48,49,55,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,92,94,100,122,123,130,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,25,25,-65,-63,25,25,25,25,25,-66,25,-14,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-67,25,25,-64,-68,-69,]),'RETORNONIVEL':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,46,48,49,55,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,92,94,100,122,123,130,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,26,26,-65,-63,26,26,26,26,26,-66,26,-14,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-67,26,26,-64,-68,-69,]),'PILA':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,46,48,49,55,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,92,94,100,122,123,130,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,27,27,-65,-63,27,27,27,27,27,-66,27,-14,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-67,27,27,-64,-68,-69,]),'SP':([3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,34,35,36,38,46,48,49,55,60,61,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,92,94,100,122,123,130,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-13,28,28,-65,-63,28,28,28,28,28,-66,28,-14,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-67,28,28,-64,-68,-69,]),'PTCOMA':([15,19,23,24,25,26,27,28,33,39,40,41,42,45,50,51,52,53,57,59,86,88,89,91,93,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,125,126,127,128,129,],[30,35,-18,-19,-20,-21,-22,-23,55,-53,61,-15,-16,-47,-48,-49,-50,-51,92,-52,-46,-33,-39,122,123,-17,-24,-25,-26,-27,-28,-30,-31,-32,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-55,-59,-29,130,-54,]),'IGUAL':([15,23,24,25,26,27,28,],[31,-18,-19,-20,-21,-22,-23,]),'PARIZQ':([16,20,21,22,31,43,47,],[32,36,37,38,44,62,87,]),'CORCHETEIZQ':([23,24,25,26,27,28,39,59,125,129,],[-18,-19,-20,-21,-22,-23,60,94,-55,-54,]),'MAS':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,67,-48,-49,-50,-51,-52,-55,-54,]),'MENOS':([23,24,25,26,27,28,31,32,36,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,46,46,46,-53,68,-48,-49,-50,-51,-52,-55,-54,]),'POR':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,69,-48,-49,-50,-51,-52,-55,-54,]),'DIVIDIDO':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,70,-48,-49,-50,-51,-52,-55,-54,]),'RESIDUO':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,71,-48,-49,-50,-51,-52,-55,-54,]),'ANDLOGICA':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,72,-48,-49,-50,-51,-52,-55,-54,]),'ORLOGICA':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,73,-48,-49,-50,-51,-52,-55,-54,]),'XOR':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,74,-48,-49,-50,-51,-52,-55,-54,]),'ANDBIT':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,75,-48,-49,-50,-51,-52,-55,-54,]),'ORBIT':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,76,-48,-49,-50,-51,-52,-55,-54,]),'XORBIT':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,77,-48,-49,-50,-51,-52,-55,-54,]),'SHIFTIZQ':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,78,-48,-49,-50,-51,-52,-55,-54,]),'SHIFTDER':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,79,-48,-49,-50,-51,-52,-55,-54,]),'IGUALIGUAL':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,80,-48,-49,-50,-51,-52,-55,-54,]),'NOIGUAL':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,81,-48,-49,-50,-51,-52,-55,-54,]),'MAYORIGUAL':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,82,-48,-49,-50,-51,-52,-55,-54,]),'MENORIGUAL':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,83,-48,-49,-50,-51,-52,-55,-54,]),'MAYOR':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,84,-48,-49,-50,-51,-52,-55,-54,]),'MENOR':([23,24,25,26,27,28,39,45,50,51,52,53,59,125,129,],[-18,-19,-20,-21,-22,-23,-53,85,-48,-49,-50,-51,-52,-55,-54,]),'PARDER':([23,24,25,26,27,28,37,39,45,50,51,52,53,54,56,58,59,62,63,64,65,66,86,88,89,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,125,127,129,],[-18,-19,-20,-21,-22,-23,57,-53,-47,-48,-49,-50,-51,90,91,93,-52,99,100,-60,-61,-62,-46,-33,-39,-24,-25,-26,-27,-28,-30,-31,-32,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,127,-55,-29,-54,]),'CORCHETEDER':([23,24,25,26,27,28,39,59,95,96,97,98,124,125,129,],[-18,-19,-20,-21,-22,-23,-53,-52,125,-56,-57,-58,129,-55,-54,]),'ARRAY':([31,],[43,]),'ABS':([31,32,36,],[47,47,47,]),'NOTLOGICA':([31,32,36,],[48,48,48,]),'NOTBIT':([31,32,36,],[49,49,49,]),'ENTERO':([31,32,36,38,46,48,49,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,94,100,],[51,51,51,51,51,51,51,96,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,96,51,]),'CADENA':([31,32,36,38,46,48,49,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,94,100,],[52,52,52,52,52,52,52,97,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,97,52,]),'DECIMAL':([31,32,36,38,46,48,49,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,100,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'FLOAT':([44,],[64,]),'INT':([44,],[65,]),'CHAR':([44,],[66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'listainstrucciones':([3,],[4,]),'simpleinstrucciones':([3,4,],[5,29,]),'declaracion':([3,4,],[6,6,]),'asignacion':([3,4,],[7,7,]),'ifcomando':([3,4,],[8,8,]),'exit':([3,4,],[9,9,]),'print':([3,4,],[10,10,]),'etiqueta':([3,4,],[11,11,]),'goto':([3,4,],[12,12,]),'read':([3,4,],[13,13,]),'unset':([3,4,],[14,14,]),'variable':([3,4,31,32,36,38,46,48,49,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,94,100,],[15,15,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'tipo':([31,],[40,]),'instruccionregistro':([31,32,36,],[41,54,56,]),'conversion':([31,],[42,]),'registro':([31,32,36,38,46,48,49,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,100,],[45,45,45,58,86,88,89,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,126,]),'acceso':([31,32,36,38,46,48,49,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,94,100,],[50,50,50,50,50,50,50,98,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,98,50,]),'dimension':([39,],[59,]),'eltipo':([44,],[63,]),'inside':([60,94,],[95,124,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> MAIN DOSPUNTOS listainstrucciones','init',3,'p_init','Gramatica.py',201),
  ('listainstrucciones -> listainstrucciones simpleinstrucciones','listainstrucciones',2,'p_lista_instrucciones','Gramatica.py',204),
  ('listainstrucciones -> simpleinstrucciones','listainstrucciones',1,'p_lista_instrucciones_simple','Gramatica.py',207),
  ('simpleinstrucciones -> declaracion','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',209),
  ('simpleinstrucciones -> asignacion','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',210),
  ('simpleinstrucciones -> ifcomando','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',211),
  ('simpleinstrucciones -> exit','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',212),
  ('simpleinstrucciones -> print','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',213),
  ('simpleinstrucciones -> etiqueta','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',214),
  ('simpleinstrucciones -> goto','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',215),
  ('simpleinstrucciones -> read','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',216),
  ('simpleinstrucciones -> unset','simpleinstrucciones',1,'p_simpleinstrucciones','Gramatica.py',217),
  ('declaracion -> variable PTCOMA','declaracion',2,'p_declaracion','Gramatica.py',219),
  ('asignacion -> variable IGUAL tipo PTCOMA','asignacion',4,'p_asignacion','Gramatica.py',221),
  ('tipo -> instruccionregistro','tipo',1,'p_tipo','Gramatica.py',223),
  ('tipo -> conversion','tipo',1,'p_tipo','Gramatica.py',224),
  ('tipo -> ARRAY PARIZQ PARDER','tipo',3,'p_tipo','Gramatica.py',225),
  ('variable -> TEMPORALES','variable',1,'p_variable','Gramatica.py',227),
  ('variable -> PARAMETROS','variable',1,'p_variable','Gramatica.py',228),
  ('variable -> DEVOLUCIONES','variable',1,'p_variable','Gramatica.py',229),
  ('variable -> RETORNONIVEL','variable',1,'p_variable','Gramatica.py',230),
  ('variable -> PILA','variable',1,'p_variable','Gramatica.py',231),
  ('variable -> SP','variable',1,'p_variable','Gramatica.py',232),
  ('instruccionregistro -> registro MAS registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',234),
  ('instruccionregistro -> registro MENOS registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',235),
  ('instruccionregistro -> registro POR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',236),
  ('instruccionregistro -> registro DIVIDIDO registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',237),
  ('instruccionregistro -> registro RESIDUO registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',238),
  ('instruccionregistro -> ABS PARIZQ registro PARDER','instruccionregistro',4,'p_instruccionregistro','Gramatica.py',239),
  ('instruccionregistro -> registro ANDLOGICA registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',240),
  ('instruccionregistro -> registro ORLOGICA registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',241),
  ('instruccionregistro -> registro XOR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',242),
  ('instruccionregistro -> NOTLOGICA registro','instruccionregistro',2,'p_instruccionregistro','Gramatica.py',243),
  ('instruccionregistro -> registro ANDBIT registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',244),
  ('instruccionregistro -> registro ORBIT registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',245),
  ('instruccionregistro -> registro XORBIT registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',246),
  ('instruccionregistro -> registro SHIFTIZQ registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',247),
  ('instruccionregistro -> registro SHIFTDER registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',248),
  ('instruccionregistro -> NOTBIT registro','instruccionregistro',2,'p_instruccionregistro','Gramatica.py',249),
  ('instruccionregistro -> registro IGUALIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',250),
  ('instruccionregistro -> registro NOIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',251),
  ('instruccionregistro -> registro MAYORIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',252),
  ('instruccionregistro -> registro MENORIGUAL registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',253),
  ('instruccionregistro -> registro MAYOR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',254),
  ('instruccionregistro -> registro MENOR registro','instruccionregistro',3,'p_instruccionregistro','Gramatica.py',255),
  ('instruccionregistro -> MENOS registro','instruccionregistro',2,'p_instruccionregistro','Gramatica.py',256),
  ('instruccionregistro -> registro','instruccionregistro',1,'p_instruccionregistro','Gramatica.py',257),
  ('registro -> acceso','registro',1,'p_registro','Gramatica.py',259),
  ('registro -> ENTERO','registro',1,'p_registro','Gramatica.py',260),
  ('registro -> CADENA','registro',1,'p_registro','Gramatica.py',261),
  ('registro -> DECIMAL','registro',1,'p_registro','Gramatica.py',262),
  ('acceso -> variable dimension','acceso',2,'p_acceso','Gramatica.py',264),
  ('acceso -> variable','acceso',1,'p_acceso','Gramatica.py',265),
  ('dimension -> dimension CORCHETEIZQ inside CORCHETEDER','dimension',4,'p_dimension','Gramatica.py',267),
  ('dimension -> CORCHETEIZQ inside CORCHETEDER','dimension',3,'p_dimension','Gramatica.py',268),
  ('inside -> ENTERO','inside',1,'p_inside','Gramatica.py',271),
  ('inside -> CADENA','inside',1,'p_inside','Gramatica.py',272),
  ('inside -> acceso','inside',1,'p_inside','Gramatica.py',273),
  ('conversion -> PARIZQ eltipo PARDER registro','conversion',4,'p_conversion','Gramatica.py',277),
  ('eltipo -> FLOAT','eltipo',1,'p_eltipo','Gramatica.py',280),
  ('eltipo -> INT','eltipo',1,'p_eltipo','Gramatica.py',281),
  ('eltipo -> CHAR','eltipo',1,'p_eltipo','Gramatica.py',282),
  ('exit -> EXIT PTCOMA','exit',2,'p_exit','Gramatica.py',285),
  ('print -> PRINT PARIZQ instruccionregistro PARDER PTCOMA','print',5,'p_print','Gramatica.py',287),
  ('etiqueta -> ETIQUETA DOSPUNTOS','etiqueta',2,'p_etiqueta','Gramatica.py',289),
  ('goto -> GOTO ETIQUETA PTCOMA','goto',3,'p_goto','Gramatica.py',291),
  ('read -> READ PARIZQ PARDER PTCOMA','read',4,'p_read','Gramatica.py',293),
  ('unset -> UNSET PARIZQ registro PARDER PTCOMA','unset',5,'p_unset','Gramatica.py',295),
  ('ifcomando -> IF PARIZQ instruccionregistro PARDER GOTO ETIQUETA PTCOMA','ifcomando',7,'p_if','Gramatica.py',297),
]
