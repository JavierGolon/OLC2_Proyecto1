# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=wildcard-import
# pylint: disable=W0614
import tkinter
import os
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import * 
from tkinter.simpledialog import *
from tkdocviewer import *
import re
# Importacion de la clase ejecucion
import Ejecucion as analisador
import Globales
Globales.initialized()
findtxt = 'Empty'
searchtxt = 'Empty'
ReporteGramatical = ['Vacio'] # es el mismo para los dos tipos
ReporteTablaSimbolos = {} # para el reporte de simbolos y el debuger
ReporteErroresInfo = {} # para el reporte de los errores en general


#============================================ CLASE PARA UTILIZAR EL TXT COMO CONSOLA DE SALIDA Y ENTRADA ======================
class txtAsConsole(object): 
	def __init__(self,text_widget):
		self.txt = text_widget
	def write(self,string):
		self.txt.insert('end',string)
		self.txt.see('end')

# =================================== CLASE PARA EL DIALOGO DE BUSCAR Y REMPLAZAR ========================



class DialogFind_Search:
	def __init__(self,parent):
		top = self.top = tkinter.Toplevel(parent)
		self.myLabel = tkinter.Label(top, text='Find')
		self.myLabel.pack()

		self.myEntryBox = tkinter.Entry(top)
		self.myEntryBox.pack()

		self.myLabel2 = tkinter.Label(top, text='Search')
		self.myLabel2.pack()

		self.myEntryBox2 = tkinter.Entry(top)
		self.myEntryBox2.pack()
		self.mySubmitButton = tkinter.Button(top, text='Submit', command=self.send)
		self.mySubmitButton.pack()
	def send(self):
		global findtxt
		global searchtxt
		findtxt = self.myEntryBox.get()
		searchtxt = self.myEntryBox2.get()
		self.top.destroy()
class Interfaz:

	__root = Tk()
	# Creamos las imagenes para los botones de los menus
	
	__imgopen = PhotoImage(file=r"Imagenes/file.png").subsample(12, 12)
	__imgnew = PhotoImage(file=r"Imagenes/carpeta.png").subsample(12, 12)
	__imgsave = PhotoImage(file=r"Imagenes/guardar.png").subsample(12, 12)
	__imgsalir = PhotoImage(file=r"Imagenes/salirimg.png").subsample(12, 12)
	__imgasc = PhotoImage(file=r"Imagenes/asc.png").subsample(12, 12)
	__imgdesc = PhotoImage(file=r"Imagenes/desc.png").subsample(12, 12)
	__imgplay = PhotoImage(file=r"Imagenes/desc.png").subsample(20, 20)
	# Creamos los marcos para las distribuciones de la ventana
	__frametop = Frame(__root)
	__framebotton = Frame(__root, width=__root.winfo_screenwidth(),
	                      height=250, background="#084B8A")
	# Creamos la pestaña
	__mytabs = ttk.Notebook(__frametop)
	# Creamos la consola
	__myConsole = Text(__framebotton, background="#000000", foreground="#FFFFFF",insertbackground='white')
	# default window width and height
	__thisWidth = 300
	__thisHeight = 300
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	__thisErroresMenu = Menu(__thisMenuBar, tearoff=0)
	__thisReportesMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEjecutarMenu = Menu(__thisMenuBar, tearoff=0)
	__thisRun = Menu(__thisMenuBar, tearoff=0)
	__ThisStop = Menu(__thisMenuBar, tearoff=0)
	__ThisNext = Menu(__thisMenuBar, tearoff=0)
	__ThisManageTabs = Menu(__thisMenuBar, tearoff=0)

	# To add scrollbar
	
	__file = None

	def __init__(self, **kwargs):

		# Set icon
		try:
				self.__root.wm_iconbitmap("Interfaz.ico")
		except:
				pass

		# Set window size (the default is 300x300)

		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.__root.title("JavGEditor")

		# Center the window
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()

		# For left-alling
		left = (screenWidth / 2) - (self.__thisWidth / 2)

		# For right-allign
		top = (screenHeight / 2) - (self.__thisHeight / 2)

		# For top and bottom
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

	

		# ===================================== DROP DOWN DE FILE ==========================================
		self.__thisFileMenu.add_command(label="New",
										command=self.__newFile, image=self.__imgnew, compound='left')
		self.__thisFileMenu.add_command(label="Open",
										command=self.__openFile, image=self.__imgopen, compound='left')
		self.__thisFileMenu.add_command(label="Save",
										command=self.__saveFile, image=self.__imgsave, compound='left')
		self.__thisFileMenu.add_separator()
		self.__thisFileMenu.add_command(label="Exit",
										command=self.__quitApplication, image=self.__imgsalir, compound='left')

		self.__thisMenuBar.add_cascade(label="File",
									menu=self.__thisFileMenu)

		# ============================================= DROP DOWN DE EDIT ===============================
		self.__thisEditMenu.add_command(label="Cut",
										command=self.__cut)
		self.__thisEditMenu.add_command(label="Copy",
										command=self.__copy)
		self.__thisEditMenu.add_command(label="Paste",
										command=self.__paste)
		self.__thisEditMenu.add_command(label="Search",
										command=self.__Search)
		self.__thisEditMenu.add_command(label="Replace",
										command=self.__Replace)

		self.__thisMenuBar.add_cascade(label="Edit",
									menu=self.__thisEditMenu)
		# ================================== DROP DOWN DE EJECUTAR ===========================================
		self.__thisEjecutarMenu.add_command(label="Ascendente",
										command=self.__FormaASC, image=self.__imgasc, compound='left')
		self.__thisEjecutarMenu.add_command(label="Descendente",
										command=self.__FormaDESC, image=self.__imgdesc, compound='left')

		self.__thisMenuBar.add_cascade(label="Execute",
									menu=self.__thisEjecutarMenu)

		# ================================= DROP DOWN REPORTES ERRORES =======================================
		self.__thisErroresMenu.add_command(label="Errores General",
										command=self.__MetodoReporteError)
		self.__thisMenuBar.add_cascade(label="Reportes Errores",
									menu=self.__thisErroresMenu)

		# ================================= DROP DOWN REPORTES ===============================================
		self.__thisReportesMenu.add_command(label="Tabla De Simbolos",
										command=self.__RTabla)
		self.__thisReportesMenu.add_command(label="Reporte AST",
										command=self.__RAst)
		self.__thisReportesMenu.add_command(label="Reporte Gramatical",
										command=self.__RGrama)

		self.__thisMenuBar.add_cascade(label="Reportes",
									menu=self.__thisReportesMenu)

		# ================================ MENU DEDUBGGER ===================================================
		self.__thisMenuBar.add_separator()
		self.__thisMenuBar.add_separator()
		self.__thisMenuBar.add_command(label="Debbug",
									command = self.__debugear)
		self.__thisMenuBar.add_separator()
		self.__thisMenuBar.add_separator()
		# ================================== DROP DOWN DE INFORMACION PERSONAL ===============================
		# POP UP de informacion personal

		self.__thisHelpMenu.add_command(label="About Developer",
										command=self.__showAbout)

		self.__thisMenuBar.add_cascade(label="Help",
									menu=self.__thisHelpMenu)

		# ===================================== MANAGE DE LAS PESTAÑAS ========================================
		self.__thisMenuBar.add_separator()
		self.__thisMenuBar.add_separator()
		self.__thisMenuBar.add_separator()
		self.__thisMenuBar.add_separator()
		self.__ThisManageTabs.add_command(label="Agregar",
										command=self.__AddTab)
		self.__ThisManageTabs.add_command(label="Eliminar",
										command=self.__DropTab)

		self.__thisMenuBar.add_cascade(label="Manage Tabs",
									menu=self.__ThisManageTabs)
		# ====================================================================================================
		# =================================== FINAL OPCIONES PARA EL MENU BAR =================================
		# =====================================================================================================

		self.__root.config(menu=self.__thisMenuBar)

		# ========================================== CONFIGURANDO LOS FRAMES =====================================
		self.__frametop.pack(side=TOP, fill=BOTH, expand=1)
		self.__framebotton.pack(side=BOTTOM, fill=NONE, expand=0)
		# ========================================== CONFIGURANDO LAS PESTAÑAS ===================================
		__web_label = Text(background="#2E2E2E", foreground="#FFFFFF",insertbackground='white')
		#__web_label.tag_configure("red",foreground="#ff0000")
		#__web_label.highlight_pattern("hola","red",)
		__web_label.bind('<Key>', self.__highlighter)
		self.__mytabs.add(__web_label, text="New Tab", padding=20)
		self.__mytabs.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.94)
		# ==================================== CONFIGURANDO LA CONSOLA =============================================
		self.__myConsole.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.94)
		sys.stdout = txtAsConsole(self.__myConsole)
		#sys.stdin = self.__myConsole

	def __quitApplication(self):
		self.__root.destroy()
		# exit()

	def __showAbout(self):
		showinfo("Proyecto 1 OLC2", "Javier Alejandro Golon Lopez \n 201700473")

	def __openFile(self):

		self.__file = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files", "*.*"),
										("Text Documents", "*.txt")])

		if self.__file == "":

			# No se pudo abrir
			self.__file = None
		else:

			# colocando el nombre del archivo en la pestaña
			self.__mytabs.tab(self.__mytabs.select(),
			                  text=os.path.basename(self.__file))
			self.__GetSelectedText().delete(1.0, END)

			file = open(self.__file, "r")
			# inserto el texto en el textarea seleccionado
			self.__GetSelectedText().insert(1.0, file.read())
			file.close()

	def __newFile(self):
		# limpio el txtarea y quito el nombre de la tab seleccionada
		self.__mytabs.tab(self.__mytabs.select(), text="Untitled")
		self.__file = None
		self.__GetSelectedText().delete(1.0, END)

	def __saveFile(self):

		if self.__file == None:
			# Abro el menu para guardar un nuevo archivo
			self.__file = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files", "*.*"),
												("Text Documents", "*.txt")])

			if self.__file == "":
				self.__file = None
			else:

				# Guardo el archivo con el texto del ultimo textarea seleccionado
				file = open(self.__file, "w")
				file.write(self.__GetSelectedText().get(1.0, END))
				file.close()

				# Cambiar el nomnbre de la pestaña
				self.__mytabs.tab(self.__mytabs.select(),
				                  text=os.path.basename(self.__file))

		else:
			file = open(self.__file, "w")
			file.write(self.__GetSelectedText().get(1.0, END))
			file.close()
	# ===================================== FUNCIONES PARA EL FUNCIONAMIENTO DE LAS OPCIONES DEL MENU ==============================
	# funcion que retorna el actual texto seleccionado

	def __GetSelectedText(self):
		actualtext = self.__mytabs.nametowidget(self.__mytabs.select())
		return actualtext

	def __cut(self):
		self.__GetSelectedText().event_generate("<<Cut>>")

	def __copy(self):
		self.__GetSelectedText().event_generate("<<Copy>>")

	def __paste(self):
		self.__GetSelectedText().event_generate("<<Paste>>")

	def __Search(self):
		theword = tkinter.simpledialog.askstring("Input","Find",parent=self.__root)
		self.PintarBusqueda(theword)

	def __Replace(self):

		mydialog = DialogFind_Search(self.__root)
		self.__root.wait_window(mydialog.top)
		txtwidget = self.__GetSelectedText()
		texto = txtwidget.get(1.0, END)
		txtwidget.delete("1.0", "end")
		if findtxt != 'Empty' and searchtxt!='Empty':
			txtwidget.insert(END,texto.replace(findtxt,searchtxt))

	#============================================================ REPORTE TABLA DE SIMBOLOS =======================
	def __RTabla(self): # reporte tabla de simbolos
		newwindow = tkinter.Toplevel(self.__root)
		tkinter.Label(newwindow, text="Reporte \n Tabla de Simbolos", font=("Arial",25)).grid(row=0, columnspan=6)
		columnas = ('Referencia','Nombre','Tipo','Valor','Ambito','Dimension')
		listbox = tkinter.ttk.Treeview(newwindow,columns=columnas,show='headings')
		for col in columnas:
			listbox.heading(col,text=col)
		listbox.grid(row=1, column=0, columnspan=4)
		for i, (llave) in enumerate(ReporteTablaSimbolos, start=1):
			tipo = ReporteTablaSimbolos[llave].tipo
			valor = ReporteTablaSimbolos[llave].valor
			listbox.insert("", "end", values=(i,llave,tipo,valor,'main',1))

	#============================================================ REPORTE GRAMATICAL ==================================
	def __RGrama(self):
		newwindow = tkinter.Toplevel(self.__root)
		tkinter.Label(newwindow, text="Reporte Gramatical \n ASC", font=("Arial",25)).grid(row=0, columnspan=6)
		columnas = ('No','Regla')
		listbox = tkinter.ttk.Treeview(newwindow,columns=columnas,show='headings')
		listbox.column("No", width=50)
		listbox.column("Regla", width=600)
		for col in columnas:
			listbox.heading(col,text=col)
		listbox.grid(row=1, column=0, columnspan=4)
		for i, (name) in enumerate(ReporteGramatical, start=1):
			listbox.insert("", "end", values=(i, name)) 

	#==================================================== REPORTE AST  ========================================
	def __RAst(self):
		newwindow = tkinter.Toplevel(self.__root)
		v = DocViewer(newwindow)
		v.pack(side="top", expand=1, fill="both")
		v.display_file("Imagenes/AST.gv.jpg") # cambiar por imagen pertinente 
	#================================================= REPORTE ERRORES GENERAL =========================================
	def __MetodoReporteError(self):
		newwindow = tkinter.Toplevel(self.__root)
		tkinter.Label(newwindow, text="Reporte \n Errores General", font=("Arial",25)).grid(row=0, columnspan=6)
		columnas = ('No','Tipo','Lexema','Descripcion','Linea','Columna')
		listbox = tkinter.ttk.Treeview(newwindow,columns=columnas,show='headings')
		for col in columnas:
			listbox.heading(col,text=col)
		listbox.grid(row=1, column=0, columnspan=4)
		for i, (llave) in enumerate(ReporteErroresInfo, start=1):
			tipo = llave.tipo
			lexema = llave.lexema
			descrip =llave.descripcion
			linea = llave.linea
			column =llave.columna 
			listbox.insert("", "end", values=(i,tipo,lexema,descrip,linea,column))  	

	def __RSema(self): # solo como ejemplo
		newwindow = tkinter.Toplevel(self.__root)
		v = DocViewer(newwindow)
		v.pack(side="top", expand=1, fill="both")
		v.display_file("Imagenes/carpeta.png") # cambiar por imagen pertinente 

	def __FormaDESC(self):
		entrada = self.__GetSelectedText().get(1.0,END)
		analisador.EjecutarDESC(entrada)
		global ReporteGramatical
		ReporteGramatical = analisador.FormaDesc.DatosGrafo
		global ReporteTablaSimbolos
		ReporteTablaSimbolos = analisador.ObtenerTablaSimbolos()
		global ReporteErroresInfo
		ReporteErroresInfo = analisador.FormaDesc.ListaE.ObtenerLista()
	def __FormaASC(self):
		
		entrada = self.__GetSelectedText().get(1.0,END)
		analisador.EjecutarASC(entrada)
		global ReporteGramatical
		ReporteGramatical = analisador.g.DatosGrafo
		global ReporteTablaSimbolos
		ReporteTablaSimbolos = analisador.ObtenerTablaSimbolos()
		global ReporteErroresInfo
		ReporteErroresInfo = analisador.g.ListaE.ObtenerLista()

		

	def __AddTab(self):
		__web_label = Text(self.__mytabs)
		__web_label.bind('<Key>', self.__highlighter)
		self.__mytabs.add(__web_label, text="New Tab", padding=20)

	def __DropTab(self):
		self.__mytabs.forget(self.__mytabs.select())

	def PintarBusqueda(self,word):
		self.__GetSelectedText().tag_remove('found', '1.0', END)
		s = word  
		if s: 
			idx = '1.0'
			while 1: #searches for desried string from index 1 
				idx = self.__GetSelectedText().search(s, idx, nocase=1,stopindex=END)  
				if not idx: break
				lastidx = '%s+%dc' % (idx, len(s))
				self.__GetSelectedText().tag_add('found', idx, lastidx)  
				idx = lastidx 
			self.__GetSelectedText().tag_config('found', foreground='#B40404')  
	# ============================================= IMPLEMENTACION DEL SINTAX HIGHLIGHT ========================================
	
	__highlightWords = {
	'if': '#DF013A',
	'else': '#DF013A',
	'main':'red',
	'exit':'red',
	'array':'#DF013A',
	'read':'#F7819F',
	'int':'#01DFA5',
	'float':'#01DFA5',
	'char':'#01DFA5',
	'print':'yellow',
	r'\(|=|\+|-|\*|\/|':'white',
	r'(\d+)':'blue',
	r'(\d+\.\d+)':'blue',
	r'\$(t|s|a|v|r)(\d+)':'#088A68',
	r'\#.*\n':'green',
	r'(\'|\").*?(\'|\")':'#DF7401'}
	def __highlighter(self,event):
		'''the highlight function, called when a Key-press event occurs'''
		for k,v in self.__highlightWords.items(): # iterate over dict
			startIndex = '1.0'
			
			while True:
				startIndex = self.__GetSelectedText().search(k, startIndex, END,regexp=True) # search for occurence of k
				if startIndex:
					endIndex = self.__GetSelectedText().index('%s+%dc' % (startIndex, (len(k)))) # find end of k
					self.__GetSelectedText().tag_add(k, startIndex, endIndex) # add tag to k
					self.__GetSelectedText().tag_config(k, foreground=v)      # and color it with v
					startIndex = endIndex # reset startIndex to continue searching
				else:
					break
	def AgregarATabla(self,treeview):
		analisador.NextDebbuger()
		# actualizo la tabla de simbolos
		ReporteTablaSimbolos = analisador.ObtenerTablaSimbolos()
		
		for i in treeview.get_children():
			treeview.delete(i)
		for i, (llave) in enumerate(ReporteTablaSimbolos, start=1):
			tipo = ReporteTablaSimbolos[llave].tipo
			valor = ReporteTablaSimbolos[llave].valor
			treeview.insert("", "end", values=(i,llave,tipo,valor,'main',1))


	def __debugear(self):
		# antes tengo que mandar a analizar la primera instruccion y traer los datos
		entrada = self.__GetSelectedText().get(1.0,END)
		analisador.DebuggerIniciar(entrada)
		global ReporteGramatical
		ReporteGramatical = analisador.g.DatosGrafo
		global ReporteTablaSimbolos
		ReporteTablaSimbolos = analisador.ObtenerTablaSimbolos()
		# abriendo la ventana que contiene la informacion
		newwindow = tkinter.Toplevel(self.__root)
		tkinter.Label(newwindow, text="Debbuger", font=("Arial",20)).grid(row=0, columnspan=6)
		columnas = ('Referencia','Nombre','Tipo','Valor','Ambito','Dimension')
		listbox = tkinter.ttk.Treeview(newwindow,columns=columnas,show='headings')
		for col in columnas:
			listbox.heading(col,text=col)
		listbox.grid(row=1, column=0, columnspan=4)
		for i, (llave) in enumerate(ReporteTablaSimbolos, start=1):
			tipo = ReporteTablaSimbolos[llave].tipo
			valor = ReporteTablaSimbolos[llave].valor
			listbox.insert("", "end", values=(i,llave,tipo,valor,'main',1))
		tkinter.Button(newwindow, text="Next", width=15, command=lambda:self.AgregarATabla(listbox)).grid(row=4, column=0)
		tkinter.Button(newwindow, text="Finish", width=15, command=None).grid(row=4, column=1)

	
	def __ThisNext(self):
		pass
	def __ThisStop(self):
		pass


	def run(self): 
		pass	
		# Run main application 
		self.__root.mainloop() 




# Run main application 
Interfaz = Interfaz(width=1100,height=800) 
Interfaz.run() 
