form = """
=======================
||  0 - Giriş Yap==> ||
||  9 - Kayıt Ol==>  ||
=======================
"""
question1 = input(form)

while True:
    if(question1 == "9"):
        print("Kayıt İşlemi.")
        name = input("Kullanıcı adınız:")
        with open("veri.txt", "a", encoding="utf-8") as dosya:
            dosya.write("{}\n".format(name))
            

        password =complex(input("Şifreniz:"))
        with open("veri.txt", "a", encoding="utf-8") as dosya2:
            dosya2.write("{}\n".format(password))
            print("kayıt başarıyla tamamlandı.")
        
    elif(question1 == "10"):
        print("çıkış yapıldı")
        exit()
    
if(question1 == "0"):

    name = input("Kullanıcı Adı Giriniz:")
    password = complex(input("Şifre Giriniz:"))


filename = 'veri.txt'
with open(filename) as f_obj:
    nameLists = f_obj.read()

if (name == nameLists.split()[0] and password == nameLists.split()[1]):
    print(name + " Giriş Başarılı")
else:
    print("Kullanıcı adı/Şifre Hatalı. ")

