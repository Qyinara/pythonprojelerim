from tkinter import *
from tkinter import messagebox
import os


pencere = Tk()

pencere.title("Erişim Portalı")

pencere.geometry("300x300")






def sign_in():
    kullanici = entry1.get()
    sifre = entry2.get()
    if (kullanici == "admin" and sifre == "erol"):
        messagebox.showinfo("", "Giriş Başarılı.")
        os.startfile('C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe')
        exit()

    elif (kullanici != "admin" and sifre == "erol"):
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı Hatalı.")
        exit()

    elif (kullanici == "admin" and sifre != "erol"):
        messagebox.showerror("Hatalı Giriş", "Şifre Hatalı")
        exit()

    else:
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı ve şifre hatalı.")
        exit()





#burası arayüz tasarımı

label1 = Label(pencere)
label1.config(text="Kullanıcı adı giriniz", font=("Ariel", 20))
label1.place(x=30, y=30)



entry1 = Entry(pencere)
entry1.place(x=80, y=80)



#-------------------------------------------------------------------


label2 = Label(pencere)
label2.config(text="Şifrenizi giriniz", font=("Ariel", 20))
label2.place(x=50, y=120)


entry2 = Entry(pencere)
entry2.place(x=80, y=170)

#----------------------------------------------------------------------


buton = Button(pencere)

buton.config(text="Giriş", bg="blue", fg="white", height="4", width="15", command=sign_in)
buton.place(relx=0.5, rely=0.9, anchor=CENTER)


mainloop()