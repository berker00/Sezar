print("NUMARA SIFRELEME & COZME PROGRAMI SEZAR ")
print("1 = SIFRE URETME ")
print("2 = SIFRE COZME")
userchs = int(input("YAPMAK ISTEDIGINIZ ISLEMI SECIN : "))
if int(userchs) == 1:
    sayi = int(input("SIFRELEMEK ISTEDIGINIZ NUMARYI GIRIN : "))
    print(sayi * 510 + 50)
elif int(userchs) == 2 :
    sayi2 = int(input("COZMEK ISTEDIGINIZ NUMARAYI GIRIN : "))
    print((sayi2 - 50) / 510)
else :
    print("GECERLI BIR ISLEM SECIN : ")

input()