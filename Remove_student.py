from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import sys

py = sys.executable

class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'livre.ico')
        self.maxsize(450,250)
        self.minsize(450,250)
        self.title("Bibliothécaire")
        a = StringVar()

        def iii():
            if len(a.get()) == 0:
                messagebox.showerror("Error", "Veuillez entrer l'ifentifiant de l'élève ")
            else:
                c = messagebox.askyesno('Remove Book', 'AEtes-vous sure de vouloir retirer cet élève ?')
                if c:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.mycursor = self.conn.cursor()
                        self.mycursor.execute("DELETE FROM students WHERE Student_Id = he201883?", [a.get()])
                        messagebox.showinfo('Remove', 'SUCCES')
                        self.conn.commit()
                        self.conn.close()
                        d = messagebox.askyesno("Confirm", "Voulez-vous retirer un autre élève?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'Remove_student.py'))
                        else:
                            self.destroy()
                    except Error:
                        messagebox.showerror("Error", "Il y a un problème")

        self.lb1= Label(self, text="Retirer un étudiant", fg = 'light blue', font=('Comic Scan Ms', 15, 'bold'))
        self.lb1.place(x=100, y=20)
        self.lb = Label(self, text="Identifiant Etudiant", font=('Comic Scan Ms', 15, 'bold'))
        self.lb.place(x=30, y=90)
        self.e1 = Entry(self, textvariable=a, width=30).place(x=260, y=98)
        self.butt1234 = Button(self, text="Retirer", width=20, command=iii).place(x=160, y=200)
Rem().mainloop()
