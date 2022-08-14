from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'livre.ico')
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Bibliothécaire")
        a = StringVar()
        def ent():
            if len(a.get()) < 5:
                messagebox.showinfo("Error","Entrez un identifiant valide")
            else:
                d = messagebox.askyesno("Confirm", "Voulez-vous retirer cet utilisateur?")
                if d:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = ?",[a.get()])
                        temp = self.myCursor.fetchone()
                        if not temp:
                            messagebox.showinfo("Oop's","Utilisateur non trouvé")
                            a.set("")
                        else:
                            self.conn.commit()
                            self.myCursor.close()
                            self.conn.close()
                            messagebox.showinfo("Confirm","Retirer avec succès")
                            a.set("")
                    except:
                        messagebox.showerror("Error","Il y a un problème")

        Label(self, text = "Retirer un utilisateur ", fg = 'light blue',font=('Arial', 15, 'bold')).place(x = 140,y = 10)
        Label(self, text = "Enter User Id: ",font=('Arial', 15, 'bold')).place(x = 20,y = 60)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 64)
        Button(self, text='Retirer', width=15, font=('arial', 10),command = ent).place(x=160, y = 150)



Rem().mainloop()