from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import sqlite3
from sqlite3 import Error
import os,sys
py=sys.executable

#créer la fenêtre
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.title("Bibliothécaire")
        self.maxsize(1366, 768)
        self.minsize(1366, 768)
        self.iconbitmap(r'livre.ico')
        self.configure(background="dark gray")
#creéer les variable
        z = StringVar()
        y = StringVar()
        x = StringVar()
        w = StringVar()
        v = StringVar()
        u = StringVar()
        s = StringVar()
        r = StringVar()

        def insert():
            try:
                self.conn = sqlite3.connect('library_administration.db')
                self.myCursor = self.conn.cursor()
                c = self.myCursor.execute("Insert into admin values (?,?,?,?,?,?,?)",[z.get(), y.get(), x.get(), w.get(), v.get(), s.get(), r.get()])
                self.conn.commit()
                self.myCursor.close()
                self.conn.close()
                if c:
                    messagebox.showinfo("Confirm", "Données ajouter avec succès")
                    self.destroy()
                    os.system('%s %s' % (py, 'Main.py'))
            except Error:
                messagebox.showinfo("Error", "Il y a un problème")
# verify input
        def verify():
            if(len(z.get())) < 5:
                messagebox.showinfo("Error","Entrer un identifiant\nl'identifiant doit dépacer 5 caractères")
            elif (len(y.get())) < 3:
                messagebox.showinfo("Error", "Entrez votre nom")
            elif (len(x.get())) < 8:
                while True:
                    if not re.search("[a-z]", x.get()):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", x.get()):
                        flag = -1
                        break
                    elif not re.search("[0-9]", x.get()):
                        flag = -1
                        break
                    elif not re.search("[_@$]", x.get()):
                        flag = -1
                        break
                    elif re.search("\s", x.get()):
                        flag = -1
                        break
                    else:
                        flag = 0
                        break
                if len(x.get()) == 0:
                    messagebox.showinfo("Error","Entrez votre mot de passe")
                elif flag == -1:
                    messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
            elif len(w.get()) == 0:
                messagebox.showinfo("Error","Selectionnez une question")
            elif len(v.get()) == 0:
                messagebox.showinfo("Error","Selectionnez une réponse")
            elif len(s.get()) == 0 or len(s.get()) > 10 or len(s.get()) < 10:
                messagebox.showinfo("Error","Entrez un numéro de GSM valide")
            elif len(s.get()) == 10:
                if s.get().isdigit():
                    cas = re.fullmatch("[6-9][0-9]{9}", s.get())
                    if cas is None:
                        messagebox.showinfo("Error","Verifier les données")
                    else:
                        insert()
#label and input
        Label(self,text="Ajouter un utilisateur",font=("Algerian",35,'bold'),fg="light blue",bg="dark gray").place(x=400,y=30)
        Label(self,text="Entrez vos données ",font=("Arial",20,'bold'),fg="light blue",bg="dark grey").place(x=570,y=130)
        Label(self, text="Identifiant", font=("Arial", 13, "bold"), bg="dark grey").place(x=420, y=260)
        Label(self, text="Nom", font=("Arial", 13, "bold"), bg="dark grey").place(x=420, y=300)
        Label(self, text="Mot de passe", font=("Arial", 13, "bold"), bg="dark grey").place(x=420, y=340)
        Label(self, text="Question de sécurité", font=("Arial", 13, "bold"), bg="dark grey").place(x=420, y=380)
        Label(self, text="Réponse", font=("Arial", 13, "bold"), bg="dark grey").place(x=420, y=420)
        Label(self, text="GSM", font=("Arial", 13, "bold"), bg="dark grey").place(x=420, y=460)
        Label(self, text="Ville", font=("Arial", 13, "bold"), bg="dark grey").place(x=760, y=460)
        Entry(self,textvariable=z,width=60).place(x=620,y=260)
        Entry(self, textvariable=y, width=60).place(x=620, y=300)
        Entry(self, show = '*',textvariable=x, width=60).place(x=620, y=340)
        ttk.Combobox(self, textvariable = w, values=["Quel est le nom de votre école?", "Quel est le nom de votre rue?","Quel est le nom de votre père?", "Quel est le nom de votre animal?"], width=57,state="readonly").place(x=620, y=380)
        Entry(self, show = '*',textvariable=v, width=60).place(x=620, y=420)
        Entry(self, textvariable=s, width=40).place(x=490, y=460)
        Entry(self, textvariable=r, width=30).place(x=805, y=460)
        Button(self, text="Enregistrer", width=10, font=("Arial", 13, "bold"), command=verify).place(x=560, y=520)
        Button(self, text="Retour", width=10, font=("Arial", 13, "bold")).place(x=720, y=520)

reg().mainloop()