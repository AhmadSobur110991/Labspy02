print ("Program untuk menentukan suatu bilangan terbesar")
print ('')
print ("NAMA  : Ahmad Sobur")
print ("KELAS : TI.19.D.2")
print ("NIM   : 311910093")
print ('')
def Ulang():
    print ('')
    a=int(input("Masukkan Bilangan 1:"))
    b=int(input("Masukkan Bilangan 2:"))
    c=int(input("Masukkan Bilangan 3:"))

    if a>b and  a>c:
        if b>c:
            print ("Bilangan Terbesarnya adalah :", a)
        else:
            print ("Bilangan Terbesarnya adalah :", a)
    elif b>a and b>c:
        if a>c:
            print ("Bilangan Terbesarnya adalah :", b)
        else:
            print ("Bilangan Terbesarnya adalah :", b)
    else:
        if a>b:
            print ("Bilangan Terbesarnya adalah :", c)
        else:
            print ("Bilangan Terbesarnya adalah :", c)

    print ('')
    print ("Mau coba lagi ? (ya / tidak)")
    x=input()
    if x== "ya":
        return Ulang()
    if x=="tidak":
        print ("Terimakasih telah menggunakan program ini.")

Ulang()
