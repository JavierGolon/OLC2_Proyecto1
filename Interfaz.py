import tkinter
import os
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
import re

class Notepad:

	__root = Tk()
	# Creamos las imagenes para los botones de los menus
	__imgnew = PhotoImage(file=r"./Imagenes/carpeta.png").subsample(12, 12)
	__imgopen = PhotoImage(file=r"./Imagenes/file.png").subsample(12, 12)
	__imgsave = PhotoImage(file=r"./Imagenes/guardar.png").subsample(12, 12)
	__imgsalir = PhotoImage(file=r"./Imagenes/salirimg.png").subsample(12, 12)
	__imgasc = PhotoImage(file=r"./Imagenes/asc.png").subsample(12, 12)
	__imgdesc = PhotoImage(file=r"./Imagenes/desc.png").subsample(12, 12)
	__imgplay = PhotoImage(file=r"./Imagenes/desc.png").subsample(20, 20)
	# Creamos los marcos para las distribuciones de la ventana
	__frametop = Frame(__root)
	__framebotton = Frame(__root, width=__root.winfo_screenwidth(),
	                      height=250, background="#084B8A")
	# Creamos la pestaña
	__mytabs = ttk.Notebook(__frametop)
	# Creamos la consola
	__myConsole = Text(__framebotton, background="#000000", foreground="#FFFFFF")
	# default window width and height
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root, width=50, height=200)
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
	__thisScrollBar = Scrollbar(__thisTextArea)
	__file = None

	def __init__(self, **kwargs):

		# Set icon
		try:
				self.__root.wm_iconbitmap("Notepad.ico")
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

		# To make the textarea auto resizable
		# self.__root.grid_rowconfigure(0, weight=1)
		# self.__root.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		# self.__thisTextArea.grid(sticky = N + E + S + W)

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
		self.__thisErroresMenu.add_command(label="Errores Lexicos",
										command=self.__RLexico)
		self.__thisErroresMenu.add_command(label="Errores Sintacticos",
										command=self.__RSinta)
		self.__thisErroresMenu.add_command(label="Errores Semanticos",
										command=self.__RSema)

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
		self.__thisMenuBar.add_cascade(label="Play",
									menu=self.__thisRun)
		self.__thisMenuBar.add_cascade(label="Stop",
									menu=self.__ThisStop)
		self.__thisMenuBar.add_cascade(label="Next",
									menu=self.__ThisNext)
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
		__web_label = Text(self.__mytabs)
		__web_label.bind('<Key>', self.__highlighter)
		self.__mytabs.add(__web_label, text="New Tab", padding=20)
		self.__mytabs.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.94)
		# ==================================== CONFIGURANDO LA CONSOLA =============================================
		self.__myConsole.place(relx=0.01, rely=0.03, relwidth=0.98, relheight=0.94)

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
		countVar = StringVar()
		pos = self.__GetSelectedText().search(
		    "a", "1.0", stopindex="end", count=countVar)
		self.__GetSelectedText().tag_add("search", pos,"%s + %sc" (pos, countVar.get()))

	def __Replace(self):
		pass

	def __RTabla(self):
		pass

	def __RAst(self):
		pass

	def __RGrama(self):
		pass

	def __RLexico(self):
		pass

	def __RSinta(self):
		pass

	def __RSema(self):
		pass

	def __FormaDESC(self):
		pass

	def __FormaASC(self):
		pass

	def __AddTab(self):
		__web_label = Text(self.__mytabs)
		__web_label.bind('<Key>', self.__highlighter)
		self.__mytabs.add(__web_label, text="New Tab", padding=20)

	def __DropTab(self):
		self.__mytabs.forget(self.__mytabs.select())
	# ============================================= IMPLEMENTACION DEL SINTAX HIGHLIGHT ========================================
	
	__highlightWords = {'if': 'green','else': 'red',re.compile('d1'):'blue'}
	def __highlighter(self,event):
		'''the highlight function, called when a Key-press event occurs'''
		for k,v in self.__highlightWords.items(): # iterate over dict
			startIndex = '1.0'
			while True:
				startIndex = self.__GetSelectedText().search(k, startIndex, END) # search for occurence of k
				if startIndex:
					endIndex = self.__GetSelectedText().index('%s+%dc' % (startIndex, (len(k)))) # find end of k
					self.__GetSelectedText().tag_add(k, startIndex, endIndex) # add tag to k
					self.__GetSelectedText().tag_config(k, foreground=v)      # and color it with v
					startIndex = endIndex # reset startIndex to continue searching
				else:
					break
	


	def run(self): 
		pass	
		# Run main application 
		self.__root.mainloop() 




# Run main application 
notepad = Notepad(width=1100,height=800) 
notepad.run() 
