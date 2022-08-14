from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import sys
py = sys.executable


#créer la fenêtre
class Add(Tk):
    def __init__(self):
        super().__init__()
    #logo de la fenêtre
        self.iconbitmap(r'livre.ico')
    #taille de la fenêtre

        self.maxsize(500, 500)
        self.minsize(500, 500)
    #titre de l'application
        self.title('Bibliothécaire')
        a = StringVar()
        b = StringVar()
        c = StringVar()

    #verifier les Input
        def b_q():
            if len(a.get()) == 0 or len(b.get()) == 0:
                messagebox.showerror("Erreur","veuillez  s'il vous plaît entrer les détails ")
            else:
                g = 1
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into books values (?,?,?,?)",[a.get(),b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Ajouter avec succès')
                    ask = messagebox.askyesno("Confirm", "Voulez-vous ajouter un autre livre ?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Veuillez svp verifier les détails")

    #créer les labels et les input box
        Label(self, text='').pack()
        Label(self, text='Ajouter un Livre', fg='dark grey', font=('Arial', 25, 'bold')).pack()
        Label(self, text='').pack()
        Label(self, text='IdLivre:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=130)
        Entry(self, textvariable=a, width=30).place(x=230, y=132)
        Label(self, text='Titre:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=180)
        Entry(self, textvariable=b, width=30).place(x=230, y=182)
        Label(self, text='Auteur:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=230)
        Entry(self, textvariable=c, width=30).place(x=230, y=232)
        Button(self, text="Submit", command=b_q).place(x=260, y=330)
Add().mainloop()