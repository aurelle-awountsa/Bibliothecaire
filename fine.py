from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import re
import sys,os
py = sys.executable


#créer la fenêtre
class Fine(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'livre.ico')
        self.maxsize(500, 300)
        self.minsize(500, 300)
        self.title("Bibliothécaire")
        #créer variables
        a = StringVar()
        def clear():
            if len(a.get()) == 0:
                messagebox.showerror("Error","Veuillez svp entrer votre identifiant")
            elif a.get().isdigit():
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Select Student_Id from students")
                    student = self.myCursor.fetchall()
                    listStudent = list(student)
                    if listStudent:
                        for sid in listStudent:
                            if int(a.get()) in sid:
                                con = messagebox.askyesno("Confirm","êtes-vous sûr de vouloir effacer l'amende?")
                                if con:
                                    self.myCursor.execute("Update students set Fine = 0 where Student_Id = ?",[a.get()])
                                    self.conn.commit()
                                    self.conn.close()
                                    messagebox.showinfo("Successful","Toutes les amendes sont effacées")
                                    d = messagebox.askyesno("Confirm","Voulez-vous effacer une autre amende?")
                                    if d:
                                        self.destroy()
                                        os.system('%s %s'% (py,'fine.py'))
                                    else:
                                        self.destroy()
                            else:
                                messagebox.showinfo("Oops","L'identifiant  saisi est introuvable")
                    else:
                        messagebox.showerror("Error","Veuillez vérifier l'identifiant")
                except:
                    messagebox.showinfo("Oops","il y a un problème")
            else:
                messagebox.showerror("Error","Veuillez vérifier l'identifiant")
        label1 = Label(self, text="Effacer l'amande", fg='dark grey', font=('Arial', 25, 'bold')).pack()
        Label(self,text="Identifiant étudiant", font = ('arial',15,'bold')).place(x=50,y=100)
        Entry(self,textvariable=a,width=40).place(x=230,y=105)
        Button(self, text='EFFACER', width=20,command = clear).place(x=230, y=155)
Fine().mainloop()