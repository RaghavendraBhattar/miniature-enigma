from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


class Notepad:
    root=Tk()
    #root.wm_iconbitmap("math.ico")
    root.title("Untitled - notepad")
    root.geometry("700x450")
    TextArea=Text(root,font=("times new roman",18))
    menubar=Menu(root)
    FileMenu=Menu(menubar,tearoff=0)
    EditMenu = Menu(menubar, tearoff=0)
    HelpMenu = Menu(menubar, tearoff=0)

    Scrollbar=Scrollbar(TextArea)
    file=None


    def __init__(self):
        # text area resizable
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.TextArea.grid(sticky=N+S+W+E)
        #filemenu
        self.FileMenu.add_command(label="New",command=self.NewFile)
        self.FileMenu.add_command(label="Open",command=self.openfile)
        self.FileMenu.add_command(label="Save",command=self.SaveFile)
        self.FileMenu.add_separator()

        self.FileMenu.add_command(label="Exit",activebackground="Red",command=self.quitApplication)

        self.menubar.add_cascade(label="File",menu=self.FileMenu)
        #EditMenu
        self.EditMenu.add_command(label="Select All",command=self.selectAll)
        self.EditMenu.add_command(label="Cut",command=self.cut)
        self.EditMenu.add_command(label="Copy",command=self.copy)
        self.EditMenu.add_command(label="Paste",command=self.paste)
        self.menubar.add_cascade(label="Edit", menu=self.EditMenu)
        #HelpMenu
        self.HelpMenu.add_command(label="About Notepad",command=self.showAbout)
        self.menubar.add_cascade(label="Help", menu=self.HelpMenu)

        self.root.config(menu=self.menubar)
        self.Scrollbar.pack(side=RIGHT,fill=Y)

        self.Scrollbar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)

    def quitApplication(self):
        self.root.destroy()

    def showAbout(self):
        showinfo("Notepad","This is Notepad Created By Raghavendra...")

    def openfile(self):
        self.file=askopenfilename(defaultextension=".txt",
                                  filetypes=[("All files","*.*"),
                                             ("text documents","*.txt")])
        if self.file == "":
            self.file= None
        else:
            self.root.title(os.path.basename(self.file)+"- Notepad")
            self.TextArea.delete(1.0,END)
            file=open(self.file,"r")
            self.TextArea.insert(1.0,file.read())
            file.close()


    def NewFile(self):
        self.root.title("Untitled - Notepad")
        self.file=None
        self.TextArea.delete(1.0,END)


    def SaveFile(self):
        if self.file ==None:
            self.file = asksaveasfilename(initialfile="Untitled.txt",
                                          defaultextension=".txt",
                                          filetype=[("All files","*.*"),
                                             ("text documents","*.txt")])
            if self.file == "":
                self.file = None
            else:
                file = open(self.file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()

                self.root.title(os.path.basename(self.file)+"- Notepad")
        else:
            file = open(self.file,"w")
            file.write(self.TextArea.get(1.0,END))
            file.close()

    def cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def selectAll(self):
        self.TextArea.event_generate("<<SelectAll>>")

    def copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def paste(self):
        self.TextArea.event_generate("<<Paste>>")








    def run(self):
        self.root.mainloop()

notepad=Notepad()
notepad.run()


