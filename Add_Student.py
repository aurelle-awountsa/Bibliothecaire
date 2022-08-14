from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
from sqlite3 import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'livre.ico')
        self.maxsize(500,500)
        self.minsize(500,500)
        self.title('Bibliothécaire')
        f = StringVar()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
#uploading image
        def convertToBinaryData(filename):
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData
#verifying input
        def asi():
            if len(f.get()) < 1:
                messagebox.showinfo("Oop's", "Veuillez entrer le numéro de votre classe")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's","Veuillez entrer votre nom")
            elif len(b.get()) < 1:
                messagebox.showinfo("Oop's", "Veuillez entrer votre identifiant")
            elif len(c.get()) < 1:
                messagebox.showinfo("Oop's", "Veuillez entrer votre classe")
            elif len(d.get()) < 10 or len(d.get()) > 10:
                messagebox.showinfo("Oop's", "Veuillez entrer votre numéro de GSM")
            elif len(e.get()) < 1:
                messagebox.showinfo("Oop's", "Veuillez selectionner une image")
            else:
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    pc = self.myCursor.execute("Insert into students('Roll_no','name','Student_Id','class','Phone_number','Image') values (?,?,?,?,?,?)",[f.get(),a.get(),b.get(),c.get(),d.get(),convertToBinaryData(e.get())])
                    self.conn.commit()
                    if pc:
                        messagebox.showinfo("Done","Etudiant ajouté avec succès")
                        ask = messagebox.askyesno("Confirm","Voulez-vous ajouter un autre étudiant?")
                        if ask:
                            self.destroy()
                            os.system('%s %s' % (py, 'Add_Student.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showerror("Error","Il y a un problème")
                    self.myCursor.close()
                    self.conn.close()
                except Error:
                    messagebox.showerror("Error","Il y a un problème")

        # label and input box
        label4 = Label(self, text='Ajouter un étudiiant', fg='dark grey', font=('Arial', 25, 'bold')).pack()
        lbl = Label(self, text='Numero de classe:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=82)
        S_name = Entry(self, textvariable=f, width=30).place(x=200, y=84)
        label = Label(self, text='Nom étudiant:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=130)
        S_name = Entry(self, textvariable=a, width=30).place(x=200, y=132)
        label5 = Label(self, text='Identifiant:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=180)
        S_ID = Entry(self, textvariable=b, width=30).place(x=200, y=182)
        label6 = Label(self, text='Classe :', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=230)
        S_Class = Entry(self, textvariable=c, width=30).place(x=200, y=232)
        label7 = Label(self, text='GSM:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=280)
        def fileDialog():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetype = (("jpeg","*.jpg"),("png","*.png"),("All Files","*.*")))
            e.set(filename)
        label8 = Label(self,text="Upload image", font=('Comic Scan Ms', 10, 'bold')).place(x=70,y=330)
        upload_image = Entry(self,textvariable = e,width = 30).place(x=200,y=330)
        butt=Button(self,text="Browse",width=7,command=fileDialog).place(x=400,y=328)
        S_phone_number = Entry(self, textvariable=d, width=30).place(x=200, y=282)
        S_butt = Button(self, text="Submit",width = 15,command=asi).place(x=230, y=390)

Add().mainloop()