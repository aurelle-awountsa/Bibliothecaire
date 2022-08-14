from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import sys

py = sys.executable

class rb(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'livre.ico')
        self.maxsize(500,250)
        self.minsize(500,250)
        self.title("Bibliothécaire")
        a = StringVar()

        def aaa():
            if len(a.get()) == 0:
                messagebox.showerror("Error","SVP entrez l'identifiant du livre")
            else:
                c = messagebox.askyesno('Remove Book', 'Etes-vous sure de vouloir retirer ce livre?')
                if c:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.mycursor = self.conn.cursor()
                        self.mycursor.execute("DELETE FROM books WHERE Book_Id = ?",[a.get()])
                        messagebox.showinfo('Remove', 'SUCCES')
                        self.conn.commit()
                        self.conn.close()
                        d = messagebox.askyesno("Confirm","Voulez-vous retirer d'autres livres?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'remove_book.py'))
                        else:
                            self.destroy()
                    except Error:
                        messagebox.showerror("Error", "Il y a un problème")
        lb1 = Label(self, text="Retirer un livre", fg = 'light blue',font=('Comic Scan Ms', 20, 'bold'))
        lb1.place(x=120, y=10)
        lb = Label(self, text="Identifiant du livre", font=('Comic Scan Ms', 20, 'bold'))
        lb.place(x=30, y=70)
        e = Entry(self, textvariable=a, width=30).place(x=300, y=80)
        bt = Button(self, text="Retirer", width=20, command=aaa).place(x=160, y=180)

rb().mainloop()
