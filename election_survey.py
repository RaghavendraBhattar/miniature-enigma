import pyodbc
from tkinter import *
from tkinter import messagebox




class DB:
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                               'Server=NANIYASH\RAGHUSQL;'
                               'Database=LEARNING;'
                               'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
       # self.cursor.execute("CREATE TABLE ELECTION_SURVEY(ID VARCHAR(50),FIRSTNAME VARCHAR(50), LASTNAME VARCHAR(50),GENDER VARCHAR(50),DOB VARCHAR(50),EMAIL VARCHAR(50), ADDRESS VARCHAR(50),DISTRICT VARCHAR(50),STATE VARCHAR(50),PIN VARCHAR(50))")
        self.conn.commit()


    def __del__(self):
        self.conn.close()


    def view(self):
        self.cursor.execute("SELECT * FROM ELECTION_SURVEY")
        rows = self.cursor.fetchall()
        return rows


    def insert(self, ID,FIRSTNAME, LASTNAME, GENDER, DOB, AGE,EMAIL, ADDRESS,DISTRICT,STATE,PIN):
        self.cursor.execute("INSERT INTO ELECTION_SURVEY VALUES(?,?,?,?,?,?,?,?,?,?,?)", (ID,FIRSTNAME, LASTNAME, GENDER, DOB,AGE, EMAIL, ADDRESS,DISTRICT,STATE,PIN))
        self.conn.commit()
        self.view()


    def update(self, ID,FIRSTNAME, LASTNAME, GENDER, DOB,AGE, EMAIL, ADDRESS,DISTRICT,STATE,PIN):
        self.cursor.execute("UPDATE ELECTION_SURVEY SET FIRSTNAME=?, LASTNAME=?, GENDER=?, DOB=?, AGE=?,EMAIL=?, ADDRESS=?,DISTRICT=?,STATE=?,PIN=? WHERE ID=?",
                        (FIRSTNAME, LASTNAME, GENDER, DOB,AGE, EMAIL, ADDRESS,DISTRICT,STATE,PIN,ID))
        self.conn.commit()
        self.view()


    def delete(self, ID):
        self.cursor.execute("DELETE FROM ELECTION_SURVEY WHERE ID=?", (ID,))
        self.conn.commit()
        self.view()


    def search(self, ID="", FIRSTNAME="", LASTNAME="", GENDER="", DOB="",AGE="", EMAIL="", ADDRESS="",DISTRICT="",STATE="",PIN=""):
        self.cursor.execute("SELECT * FROM ELECTION_SURVEY WHERE ID=? OR FIRSTNAME=? OR LASTNAME=? OR GENDER=? OR DOB=? OR AGE=? OR EMAIL=? OR ADDRESS=? OR DISTRICT=? OR STATE=? OR PIN=?",
                        (ID,FIRSTNAME, LASTNAME, GENDER, DOB, AGE,EMAIL, ADDRESS,DISTRICT,STATE,PIN))
        rows = self.cursor.fetchall()
        return rows

    def filter(self, GENDER="", AGE="",  DISTRICT="", STATE=""):
        self.cursor.execute("SELECT * FROM ELECTION_SURVEY WHERE GENDER=? OR AGE<=? or DISTRICT=? OR STATE=?",(GENDER,AGE,DISTRICT,STATE))
        rows = self.cursor.fetchall()
        return rows




db = DB()


def VOTERSRec(event):
    global selected_tuple
    index = VOTERSlist.curselection()[0]
    selected_tuple = VOTERSlist.get(index)
    TXTID.delete(0, END)
    TXTID.insert(END, selected_tuple[0])

    TXTFIRSTNAME.delete(0, END)
    TXTFIRSTNAME.insert(END, selected_tuple[1])
    TXTLASTNAME.delete(0, END)
    TXTLASTNAME.insert(END, selected_tuple[2])
    TXTGENDER.delete(0, END)
    TXTGENDER.insert(END, selected_tuple[3])
    TXTDOB.delete(0, END)
    TXTDOB.insert(END, selected_tuple[4])
    TXTAGE.delete(0, END)
    TXTAGE.insert(END, selected_tuple[5])
    TXTEMAIL.delete(0, END)
    TXTEMAIL.insert(END, selected_tuple[6])
    TXTADRESS.delete(0, END)
    TXTADRESS.insert(END, selected_tuple[7])
    TXTDISTRICT.delete(0, END)
    TXTDISTRICT.insert(END, selected_tuple[8])
    TXTSTATE.delete(0, END)
    TXTSTATE.insert(END, selected_tuple[9])
    TXTPINCODE.delete(0, END)
    TXTPINCODE.insert(END, selected_tuple[10])


def clearData():
    TXTID.delete(0, END)
    TXTFIRSTNAME.delete(0, END)
    TXTLASTNAME.delete(0, END)
    TXTGENDER.delete(0, END)
    TXTDOB.delete(0, END)
    TXTAGE.delete(0,END)
    TXTEMAIL.delete(0, END)
    TXTADRESS.delete(0, END)
    TXTDISTRICT.delete(0, END)
    TXTSTATE.delete(0, END)
    TXTPINCODE.delete(0, END)

def exit():
    window.destroy()

def view_command():
    VOTERSlist.delete(0, END)
    for row in db.view():
        VOTERSlist.insert(END, row)

def search_command():
    VOTERSlist.delete(0, END)
    for row in db.search(ID.get(),FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), DOB.get(),AGE.get(),EMAIL.get(),ADDRESS.get(),DISTRICT.get(),STATE.get(),PIN.get()):
        VOTERSlist.insert(END, row)


def add_command():
    db.insert(ID.get(),FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), DOB.get(),AGE.get(),EMAIL.get(),ADDRESS.get(),DISTRICT.get(),STATE.get(),PIN.get())
    VOTERSlist.delete(0, END)
    VOTERSlist.insert(END, (ID.get(),FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), DOB.get(),AGE.get(),EMAIL.get(),ADDRESS.get(),DISTRICT.get(),STATE.get(),PIN.get()))

def delete_command():

    db.delete(ID.get())
    VOTERSlist.delete(0, END)
    TXTID.delete(0, END)

def update_command():
   db.update(ID.get(),FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), DOB.get(),AGE.get(),EMAIL.get(),ADDRESS.get(),DISTRICT.get(),STATE.get(),PIN.get())
   VOTERSlist.delete(0, END)
   VOTERSlist.insert(END, (ID.get(),FIRSTNAME.get(), LASTNAME.get(), GENDER.get(), DOB.get(),AGE.get(),EMAIL.get(),ADDRESS.get(),DISTRICT.get(),STATE.get(),PIN.get()))
   #return clearData()

def filter_command():
    VOTERSlist.delete(0, END)
    for row in db.filter( GENDER.get(), AGE.get(),DISTRICT.get(),STATE.get()):
        VOTERSlist.insert(END, row)
#image=PhotoImage(file='C:\\Users\\Admin\\Desktop\\184974.jpg')










# ==========================================FRAMES=====================================================================================
window=Tk()
window.title("Election Survey 2019")
window.geometry("1450x750+0+0")
window.config(bg="aquamarine2")


MainFrame = Frame(window, bg="aquamarine2",width=1450, height=800, padx=18, pady=10, relief=RIDGE)

MainFrame.grid()

TitFrame = Frame(MainFrame, bd=5, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
TitFrame.pack(side=TOP)

lblTit = Label(TitFrame, font=('Times New Roman', 45, 'bold'), text="ELECTION SURVEY",
                    bg="Ghost White")
lblTit.grid(sticky=W)

ButtonFrame = Frame(MainFrame, bd=5, width=1250, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
ButtonFrame.pack(side=BOTTOM)

DataFrame = Frame(MainFrame, bd=5, width=1400, height=200, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
DataFrame.pack(side=BOTTOM)

DataFrameLeft = LabelFrame(DataFrame, bd=3, width=850, height=400, padx=30, bg="Ghost White", relief=RIDGE,
                           font=('Times New Roman', 20, 'bold'), text="VOTER DATA\n")
DataFrameLeft.pack(side=LEFT)

DataFrameRight = LabelFrame(DataFrame, bd=3, width=450, height=400, padx=31, pady=3, bg="Ghost white",
                            relief=RIDGE, font=('Times New Roman', 20, 'bold'), text="VOTER LIST\n")
DataFrameRight.pack(side=RIGHT)

# ==========================================FRAMES=====================================================================================
def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing
ID=StringVar()
FIRSTNAME=StringVar()
LASTNAME=StringVar()
GENDER=StringVar()
DOB=StringVar()
AGE=StringVar()
EMAIL=StringVar()
ADDRESS=StringVar()
DISTRICT=StringVar()
STATE=StringVar()
PIN=StringVar()

LBID= Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="ID:", padx=2, pady=2,
                           bg="Ghost White")
LBID.grid(row=0, column=0, sticky=W)
TXTID = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=ID, width=19)
TXTID.grid(row=0, column=1)

LBFIRSTNAME = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="FIRSTNAME:", padx=2, pady=2,
                         bg="Ghost White")
LBFIRSTNAME.grid(row=1, column=0, sticky=W)
TXTFIRSTNAME = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=FIRSTNAME, width=19)
TXTFIRSTNAME.grid(row=1, column=1)

LBLASTNAME = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="LASTNAME:", padx=2, pady=2,
                         bg="Ghost White")
LBLASTNAME.grid(row=2, column=0, sticky=W)
TXTLASTNAME = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=LASTNAME, width=19)
TXTLASTNAME.grid(row=2, column=1)

LBGENDER = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="GENDER:", padx=2, pady=2,
                           bg="Ghost White")
LBGENDER.grid(row=3, column=0, sticky=W)
TXTGENDER = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=GENDER, width=19)
TXTGENDER.grid(row=3, column=1)

LBDOB= Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="DOB:", padx=2, pady=2,
                           bg="Ghost White")
LBDOB.grid(row=4, column=0, sticky=W)
TXTDOB = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=DOB, width=19)
TXTDOB.grid(row=4, column=1)

LBAGE= Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="AGE:", padx=2, pady=2,
                           bg="Ghost White")
LBAGE.grid(row=5, column=0, sticky=W)
TXTAGE = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=AGE, width=19)
TXTAGE.grid(row=5, column=1)

LBEMAIL = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="EMAIL:", padx=2, pady=2,
                           bg="Ghost White")
LBEMAIL.grid(row=6, column=0, sticky=W)
TXTEMAIL = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=EMAIL, width=19)
TXTEMAIL.grid(row=6, column=1)

LBADRESS = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="ADDRESS:", padx=2, pady=2,
                            bg="Ghost White")
LBADRESS.grid(row=7, column=0, sticky=W)
TXTADRESS = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=ADDRESS, width=19)
TXTADRESS.grid(row=7, column=1)

LBDISTRICT = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="DISTRICT:", padx=2, pady=2,
                            bg="Ghost White")
LBDISTRICT.grid(row=8, column=0, sticky=W)
TXTDISTRICT = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=DISTRICT, width=19)
TXTDISTRICT.grid(row=8, column=1)

LBSTATE = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="STATE:", padx=2, pady=2,
                            bg="Ghost White")
LBSTATE.grid(row=9, column=0, sticky=W)
TXTSTATE = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=STATE, width=19)
TXTSTATE.grid(row=9, column=1)

LBPINCODE = Label(DataFrameLeft, font=('Times New Roman', 13, 'bold'), text="PIN CODE:", padx=2, pady=2,
                              bg="Ghost White")
LBPINCODE.grid(row=10, column=0, sticky=W)
TXTPINCODE = Entry(DataFrameLeft, font=('Times New Roman', 13, 'bold'), textvariable=PIN, width=19)
TXTPINCODE.grid(row=10, column=1)

# ==========================================LIST BOX AND SCROLL BOX=================================================================

scrollbar = Scrollbar(DataFrameRight)
scrollbar.grid(row=0, column=1, sticky='ns')

VOTERSlist = Listbox(DataFrameRight, width=90, height=16, font=('Times New Roman', 13, 'bold'), yscrollcommand=scrollbar.set)
VOTERSlist.bind('<<ListboxSelect>>', VOTERSRec)
VOTERSlist.grid(row=0, column=0, padx=8)
scrollbar.config(command=VOTERSlist.yview)

# ==========================================LIST BOX AND SCROLL BOX=================================================================

btnAddData = Button(ButtonFrame, text="Add New", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=add_command)
btnAddData.grid(row=0, column=0)
btnDisplayData = Button(ButtonFrame, text="Display", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=view_command)
btnDisplayData.grid(row=0, column=1)
btnclearData = Button(ButtonFrame, text="Clear", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=clearData)
btnclearData.grid(row=0, column=2)
btnDeleteData = Button(ButtonFrame, text="Delete", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=delete_command)
btnDeleteData.grid(row=0, column=3)
btnsearchData = Button(ButtonFrame, text="Search", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=search_command)
btnsearchData.grid(row=0, column=4)
btnupdate = Button(ButtonFrame, text="Update", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=update_command)
btnupdate.grid(row=0, column=5)
btnfilter = Button(ButtonFrame, text="FILTER", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=filter_command)
btnfilter.grid(row=0, column=6)

btnExit = Button(ButtonFrame, text="Exit", font=('Times New Roman', 13, 'bold'), width=14, height=1, bd=4,command=exit)
btnExit.grid(row=0, column=7)









window.mainloop()