from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Erişim Portalı")
pencere.geometry("300x300")




def sign_in():
    kullanici = entry1.get()
    sifre = entry2.get()
    if (kullanici == "admin" and sifre == "erol"):
        messagebox.showinfo("", "Giriş Başarılı.")
        label1.destroy()
        entry1.destroy()
        entry2.destroy()
        buton.destroy()
        exit()
    elif (kullanici != "admin" and sifre == "erol"):
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya Şifre Hatalı.")
        label1.destroy()
        entry1.destroy()
        entry2.destroy()
        buton.destroy()
        exit()
    elif (kullanici == "admin" and sifre != "erol"):
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya Şifre Hatalı.")
        label1.destroy()
        entry1.destroy()
        entry2.destroy()
        buton.destroy()
        exit()
    elif (kullanici != "admin" and sifre != "erol"):
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya Şifre Hatalı.")
        label1.destroy()
        entry1.destroy()
        entry2.destroy()
        buton.destroy()
        exit()





#burası Arayüz tasarımı

label1 = Label(pencere)

label1.config(text="Kullanıcı adı giriniz.", font=("Arial", 20))

label1.place(x=30, y=20)




entry1=Entry(pencere)

entry1.place(x=80, y=70)


#------------------------------------------------------------

label2 = Label(pencere)

label2.config(text="Şifrenizi giriniz.", font=("Arial", 20))

label2.place(x=50, y=120)




entry2 = Entry(pencere)

entry2.place(x=80, y=170)


#------------------------------------------------------------


buton = Button(pencere)

buton.config(text="Giriş yap", bg="brown", fg="white", height="4",width="15", command=sign_in)

buton.place(relx=0.5, rely=0.9, anchor=CENTER)


mainloop()



