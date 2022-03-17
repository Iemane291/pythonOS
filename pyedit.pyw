# Importing Required libraries and Modules
import platform
import json

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path

# this is my 9th time using classes :\
text_name = "pyEdit"
geometry = "768x630"


class TextEditor:

    def getOption(self, optionName):
        weirdPath = Path("data")
        with open(weirdPath / "settings.json", "r") as f:
            return json.load(f).get(optionName)
    # Defining Constructor
    def __init__(self, root):
        # Assigning root
        self.root = root
        # Title of the window
        self.root.title(text_name)
        # Window Geometry
        self.root.geometry(geometry)
        # Initializing filename
        self.filename = None
        # Declaring Title variable
        self.title = StringVar()

        self.lang = self.getOption("language")

        self.root.iconphoto(False, PhotoImage(file='icons/pyedit/window-icon.png'))

        self.cascades = ["File", "Edit", "Help"]
        if self.lang == "spanish-gt":
            self.cascades = ["Archivo", "Editar", "Ayuda"]

        # Declaring Status variable
        self.status = StringVar()
        # Creating Titlebar
        self.titlebar = Label(
            self.root,
            textvariable=self.title,
            font=("Product Sans", 15, "bold"),
            bd=2,
            relief=GROOVE,
        )
        # Packing Titlebar to root window
        self.titlebar.pack(side=TOP, fill=BOTH)
        # Calling Settitle Function
        self.settitle()
        # Creating Statusbar
        self.statusbar = Label(
            self.root,
            textvariable=self.status,
            font=("decotype-naskh.ttf", 15),
            bd=2,
            relief=GROOVE,
        )
        # Packing status bar to root window
        self.statusbar.pack(side=BOTTOM, fill=BOTH)
        # Initializing Status
        self.status.set("pyEdit")
        # Creating Menubar
        self.menubar = Menu(self.root, activebackground="skyblue")
        # Configuring menubar on root window
        self.root.config(menu=self.menubar)
        # Creating File Menu
        self.filemenu = Menu(
            self.menubar,
            activebackground="skyblue",
            tearoff=0,
        )

        self.fileMenuNames = ["New", "Open", "Save", "Save As"]
        if self.lang == "spanish-gt":
            self.fileMenuNames = ["Nuevo", "Abrir", "Guardar", "Guardar como", "Salida"]

        # Adding New file Command
        self.filemenu.add_command(
            label=self.fileMenuNames[0], accelerator="Ctrl+N", command=self.newfile
        )
        # Adding Open file Command
        self.filemenu.add_command(
            label=self.fileMenuNames[1], accelerator="Ctrl+O", command=self.openfile
        )
        # Adding Save File Command
        self.filemenu.add_command(
            label=self.fileMenuNames[2], accelerator="Ctrl+S", command=self.savefile
        )
        # Adding Save As file Command
        self.filemenu.add_command(
            label=self.fileMenuNames[3], accelerator="Ctrl+A", command=self.saveasfile
        )
        # Adding Seprator
        self.filemenu.add_separator()
        # Adding Exit window Command
        self.filemenu.add_command(label=self.fileMenuNames[4], accelerator="Ctrl+E", command=self.exit)
        # Cascading filemenu to menubar
        self.menubar.add_cascade(label=self.cascades[0], menu=self.filemenu)
        # Creating Edit Menu
        self.editmenu = Menu(
            self.menubar,
            activebackground="skyblue",
            tearoff=0,
        )

        self.editMenuNames = ["Cut", "Copy", "Paste", "Undo", "Edit"]
        if self.lang == "spanish-gt":
            self.editMenuNames = ["Cortar", "Copiar", "Pegar", "Deshacer", "Editar"]
        # Adding Cut text Command
        self.editmenu.add_command(label=self.editMenuNames[0], accelerator="Ctrl+X", command=self.cut)
        # Adding Copy text Command
        self.editmenu.add_command(label=self.editMenuNames[1], accelerator="Ctrl+C", command=self.copy)
        # Adding Paste text command
        self.editmenu.add_command(
            label=self.editMenuNames[2], accelerator="Ctrl+V", command=self.paste
        )
        # Adding Seprator
        self.editmenu.add_separator()
        # Adding Undo text Command
        self.editmenu.add_command(label=self.editMenuNames[3], accelerator="Ctrl+U", command=self.undo)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label=self.editMenuNames[4], menu=self.editmenu)
        # Creating Help Menu
        self.helpmenu = Menu(
            self.menubar,
            activebackground="skyblue",
            tearoff=0,
        )

        self.helpMenuName = "About"
        if self.lang == "spanish-gt":
            self.helpMenuName = "Sobre"
        # Adding About Command
        self.helpmenu.add_command(label=self.helpMenuName, command=self.infoabout)
        # Cascading helpmenu to menubar
        self.menubar.add_cascade(label=self.cascades[2], menu=self.helpmenu)
        # Creating Scrollbar
        scrol_y = Scrollbar(self.root, orient=VERTICAL)
        # Creating Text Area
        self.txtarea = Text(
            self.root,
            yscrollcommand=scrol_y.set,
            font=("Consolas", 15, "bold"),
            state="normal",
            relief=GROOVE,
        )
        # Packing scrollbar to root window
        scrol_y.pack(side=RIGHT, fill=Y)
        # Adding Scrollbar to text area
        scrol_y.config(command=self.txtarea.yview)
        # Packing Text Area to root window
        self.txtarea.pack(fill=BOTH, expand=1)
        # Calling shortcuts funtion
        self.shortcuts()

    # Defining settitle function
    def settitle(self):
        # Checking if Filename is not None
        if self.filename:
            # Updating Title as filename
            self.title.set(self.filename)
        else:
            # Updating Title as Untitled
            if self.lang == "english":
                self.title.set("Untitled")
            elif self.lang == "spanish-gt":
                self.title.set("Intitulado")

    # Defining New file Function
    def newfile(self, *args):
        # Clearing the Text Area
        self.txtarea.delete("1.0", END)
        # Updating filename as None
        self.filename = None
        # Calling settitle funtion
        self.settitle()
        # updating status
        if self.lang == "english":
            self.status.set("New File Created")
        elif self.lang == "spanish-gt":
            self.status.set("Nuevo archivo creado")

    # Defining Open File Funtion
    def openfile(self, *args):
        # Exception handling
        try:
            self.fileNameTitle = "Select file"
            if self.lang == "spanish-gt":
                self.fileNameTitle = "Seleccione Archivo"
            

            filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py"), ("Lua Files", "*.lua"))

            if self.lang == "spanish-gt":
                filetypes = (("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt"), ("Archivos Python", "*.py"), ("Archivos Lua", "*.lua "))

            # Asking for file to open
            self.filename = filedialog.askopenfilename(
                title="Select file",
                filetypes=filetypes,
            )
            # checking if filename not none
            if self.filename:
                # opening file in readmode
                infile = open(self.filename, "r")
                # Clearing text area
                self.txtarea.delete("1.0", END)
                # Inserting data Line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing the file
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Opened Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    # Defining Save File Funtion
    def savefile(self, *args):
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Reading the data from text area
                data = self.txtarea.get("1.0", END)
                # opening File in write mode
                outfile = open(self.filename, "w")
                # Writing Data into file
                outfile.write(data)
                # Closing File
                outfile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                if self.lang == "english":
                    self.status.set("Saved Successfully")
                elif self.lang == "spanish-gt":
                    self.status.set("Guardado exitosamente")
            else:
                self.saveasfile()
        except Exception as e:
            if self.lang == "english":
                messagebox.showerror("Exception", e)
            elif self.lang == "spanish-gt":
                messagebox.showerror("Excepción", e)

    # Defining Save As File Funtion
    def saveasfile(self, *args):
        # Exception handling
        try:
            filetypes = (("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py"), ("Lua Files", "*.lua"))

            if self.lang == "spanish-gt":
                filetypes = (("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt"), ("Archivos Python", "*.py"), ("Archivos Lua", "*.lua "))
            self.initialFile = "Untitled"
            if self.lang == "spanish-gt":
                self.initialFile = "Intitulado"
            
            self.filenametitle = "Save file as"
            if self.lang == "spanish-gt":
                self.filenametitle = "Guardar archivo como"
            # Asking for file name and type to save
            untitledfile = filedialog.asksaveasfilename(
                title=self.filenametitle,
                defaultextension=".txt",
                initialfile=self.initialFile,
                filetypes=filetypes,
            )
            # Reading the data from text area
            data = self.txtarea.get("1.0", END)
            # opening File in write mode
            outfile = open(untitledfile, "w")
            # Writing Data into file
            outfile.write(data)
            # Closing File
            outfile.close()
            # Updating filename as Untitled
            self.filename = untitledfile
            # Calling Set title
            self.settitle()
            # Updating Status
            if self.lang == "spanish-gt":
                self.status.set("Guardado exitosamente")
            elif self.lang == "english":
                self.status.set("Saved successfully")
        except Exception as e:
            if self.lang == "english":
                messagebox.showerror("Exception", e)
            elif self.lang == "spanish-gt":
                messagebox.showerror("Excepción", e)

    # Defining Exit Funtion
    def exit(self, *args):
        if self.lang == "english":
            op = messagebox.askyesno("WARNING", "! You will loose your changes")
        elif self.lang == "spanish-gt":
            op = messagebox.askyesno("ADVERTENCIA", "¡Perderás tus cambios!")
        if op > 0:
            self.root.destroy()
        else:
            return

    # Defining Cut Funtion
    def cut(self, *args):
        self.txtarea.event_generate("<<Cut>>")

    # Defining Copy Funtion
    def copy(self, *args):
        self.txtarea.event_generate("<<Copy>>")

    # Defining Paste Funtion
    def paste(self, *args):
        self.txtarea.event_generate("<<Paste>>")

    # Defining Undo Funtion
    def undo(self, *args):
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Clearing Text Area
                self.txtarea.delete("1.0", END)
                # opening File in read mode
                infile = open(self.filename, "r")
                # Inserting data Line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing File
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                if self.lang == "english":
                    self.status.set("Task Undone Successfully")
                elif self.lang == "spanish-gt":
                    self.status.set("Tarea deshecha con éxito")
            else:
                # Clearing Text Area
                self.txtarea.delete("1.0", END)
                # Updating filename as None
                self.filename = None
                # Calling Set title
                self.settitle()
                # Updating Status
                if self.lang == "english":
                    self.status.set("Undone Successfully")
                elif self.lang == "spanish-gt":
                    self.status.set("deshecho con éxito")
        except Exception as e:
            if self.lang == "english":
                messagebox.showerror("Exception", e)
            elif self.lang == "spanish-gt":
                messagebox.showerror("Excepción", e)

    # Defining About Funtion
    def infoabout(self):
        messagebox.showinfo(
            "Sobre",
            "pyEdit es un programa hecho para ser como el Bloc de notas, pyEdit es un programa en pythonOS.",
        )

    # Defining shortcuts Funtion
    def shortcuts(self):
        shortcut1 = "<Control-n>"
        shortcut2 = "<Control-o>"
        shortcut3 = "<Control-s>"
        shortcut4 = "<Control-a>"
        shortcut5 = "<Control-e>"
        shortcut6 = "<Control-x>"
        shortcut7 = "<Control-c>"
        shortcut8 = "<Control-v>"
        shortcut9 = "<Control-u>"
        if platform.system() == "Darwin":
            shortcut1 = "<Command-n>"
            shortcut2 = "<Command-o>"
            shortcut3 = "<Command-s>"
            shortcut4 = "<Command-a>"
            shortcut5 = "<Command-e>"
            shortcut6 = "<Command-x>"
            shortcut7 = "<Command-c>"
            shortcut8 = "<Command-v>"
            shortcut9 = "<Command-u>"
        # Binding Ctrl+n to newfile funtion
        self.txtarea.bind(shortcut1, self.newfile)
        # Binding Ctrl+o to openfile funtion
        self.txtarea.bind(shortcut2, self.openfile)
        # Binding Ctrl+s to savefile funtion
        self.txtarea.bind(shortcut3, self.savefile)
        # Binding Ctrl+a to saveasfile funtion
        self.txtarea.bind(shortcut4, self.saveasfile)
        # Binding Ctrl+e to exit funtion
        self.txtarea.bind(shortcut5, self.exit)
        # Binding Ctrl+x to cut funtion
        self.txtarea.bind(shortcut6, self.cut)
        # Binding Ctrl+c to copy funtion
        self.txtarea.bind(shortcut7, self.copy)
        # Binding Ctrl+v to paste funtion
        self.txtarea.bind(shortcut8, self.paste)
        # Binding Ctrl+u to undo funtion
        self.txtarea.bind(shortcut9, self.undo)


# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()
