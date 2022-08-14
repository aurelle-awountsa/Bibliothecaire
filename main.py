from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import sys
from tkinter import ttk
py=sys.executable

#créer la fenêtre
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'livre.ico')
        self.configure(bg='light blue')
        self.maxsize(1366, 768)
        self.minsize(1366, 768)
        self.state('zoomed')
        self.title('Bibliothécaire')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
#appel des pages


        def a_s(MainWin):
            from Add_Student import  Add



        def a_b(MainWin):
            from Add_Books import  Add

        def r_b(MainWin):
            from remove_book import rb

        def r_s(MainWin):
            from Remove_student import  Rem

        def ib(MainWin):
            from issueTable import  issue

        def rb1(MainWin):
            from renew import renew

        def ret(MainWin):
            from ret import ret


        def sea(MainWin):
            from Search import Sea

        # def handle(event):
        #     if self.listTree.identify_region(event.x,event.y) == "separator":
        #         return "break"
        def add_user(MainWin):
            from Reg import reg
        def rem_user(MainWin):
            from Rem import Rem
        def cfine(MainWin):
            from fine import Fine
        def sest(MainWin):
           from  Search_Student import  Sst

#creating table

        self.listTree = ttk.Treeview(self,height=13,columns=('SID','Name','Fine','Book Name','Issue Date','Return Date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0",text='ID Livre',anchor = 'center')
        self.listTree.column("#0",width=100,minwidth=100,anchor='center')
        self.listTree.heading("#1", text='Id étudiant')
        self.listTree.column("#1",width=100,minwidth=100,anchor='center')
        self.listTree.heading("Name", text='Nom étudiant')
        self.listTree.column("Name", width=150,minwidth=150,anchor='center')
        self.listTree.heading("Fine", text='Amende')
        self.listTree.column("Fine", width=100,minwidth=100,anchor='center')
        self.listTree.heading("Book Name", text='Nom Livre')
        self.listTree.column("Book Name", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Return Date", text='Date Retour')
        self.listTree.column("Return Date", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Issue Date", text='Date publié')
        self.listTree.column("Issue Date", width=125, minwidth=125,anchor='center')
        # self.listTree.bind('<Button-1>',handle) if you don't want to expand column activat this and the above handle function
        self.listTree.place(x=40,y=400)
        self.vsb.place(x=943,y=400,height=287)
        self.hsb.place(x=41,y=687,width=902)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))

        list1 = Menu(self)
        list1.add_command(label="Etudiant", command=lambda MainWin=MainWin :a_s(MainWin))
        list1.add_command(label="Livre", command=lambda MainWin=MainWin :a_b(MainWin))

        list2 = Menu(self)
        list2.add_command(label="Etudiant",command=lambda MainWin=MainWin :r_s(MainWin))
        list2.add_command(label="Livre", command=lambda MainWin=MainWin :r_b(MainWin))

        list3 = Menu(self)
        list3.add_command(label = "Ajouter un utilisateur",command=lambda MainWin=MainWin :add_user(MainWin))
        list3.add_command(label = "Retirer un utilisateur",command=lambda MainWin=MainWin :rem_user(MainWin))
        list3.add_command(label = "Effacer une amende",command=lambda MainWin=MainWin :cfine(MainWin))

        self.mymenu.add_cascade(label='Ajouter', menu=list1)
        self.mymenu.add_cascade(label='Retirer', menu=list2)
        self.mymenu.add_cascade(label = 'Outils Admin', menu = list3)

        self.config(menu=self.mymenu)

        def ser():
            try:
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                self.change = int(self.a.get())
                self.myCursor.execute("Select issue.BID,issue.SID,students.name,students.Fine,books.Book_name,issue.Issue_date,issue.Return_date from books,students,issue where issue.BID = books.Book_Id and SID = ?",[self.change])
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in self.pc:
                        self.listTree.insert("",'end',text=row[0] ,values = (row[1],row[2],row[3],row[4],row[5],row[6]))
                else:
                    messagebox.showinfo("Error", "Soit l'ID est erroné, soit le livre n'a pas encore été publié sous cet ID.")
            except Error:
                messagebox.showerror("Error","il y a un problème")
        def ent():
            try:
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Select issue.BID,issue.SID,students.name,students.Fine,books.Book_name,issue.Issue_date,issue.Return_date from books,students, issue where issue.BID = books.Book_Id and BID = ?",[self.b.get()])
                self.pc = self.myCursor.fetchall()
                if self.pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in self.pc:
                        self.listTree.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4], row[5],row[6]))
                else:
                    messagebox.showinfo("Error", "Entrer un identifiant valide")
            except Error:
                messagebox.showerror("Error", "il y a un problème")

        def check():
            try:
                conn = sqlite3.connect('library_administration.db')
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Veuillez svp enregistrer l'utilisateur")
                    x = messagebox.askyesno("Confirm","Voulez-vous enregistrer un utilisateur?")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Reg.py'))
                else:
                    #label and input box
                    self.label3 = Label(self, text='Bienvenue sur Bibliothécaire', bg='light blue', font=('Algerian', 45, 'bold'))
                    self.label3.place(x=290, y=80)
                    self.label4 = Label(self, text="Entret l'id étudiant", bg='light blue', font=('Arial', 20, 'bold'))
                    self.label4.place(x=100, y=200)
                    self.e1 = Entry(self, textvariable=self.a, width=40).place(x=400, y=210)
                    self.srt = Button(self, text='Recherche', width=15, font=('arial', 10),command = ser).place(x=700, y=206)
                    self.label5 = Label(self, text='OU', bg='light blue', font=('arial', 16, 'bold')).place(x=170, y=235)
                    self.label5 = Label(self, text="Entrer l'id du livre", bg='light blue', font=('Arial', 20, 'bold'))
                    self.label5.place(x=100, y=260)
                    self.e2 = Entry(self, textvariable=self.b, width=40).place(x=400, y=270)
                    self.brt = Button(self, text='Trouver', width=15, font=('arial', 10),command = ent).place(x=700, y=266)
                    self.label6 = Label(self, text="Details", bg='light blue', font=('Arial', 15, 'underline', 'bold'))
                    self.label6.place(x=20, y=350)
                    self.button = Button(self, text='Chercher un étudiant', width=20, font=('Algerian', 20), command=lambda MainWin=MainWin :sest(MainWin)).place(x=1000,y=250)
                    self.button = Button(self, text='Chercher un livre', width=20, font=('Algerian', 20), command=lambda MainWin=MainWin :sea(MainWin)).place(x=1000,y=350)
                    self.brt = Button(self, text="Confier un livre", width=20, font=('Algerian', 20), command=lambda MainWin=MainWin :ib(MainWin)).place(x=1000, y=450)
                    self.brt = Button(self, text="Renouveller un livre", width=20, font=('Algerian', 20), command=lambda MainWin=MainWin :rb1(MainWin)).place(x=1000, y=550)
                    self.brt = Button(self, text="Retourner un livre", width=20, font=('Algerian', 20), command=lambda MainWin=MainWin :ret(MainWin)).place(x=1000, y=650)
            except Error:
                messagebox.showerror("Error", "il ya un problème")
        check()

MainWin().mainloop()