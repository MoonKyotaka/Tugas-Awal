# MEMBUAT PROGRAM PENENTU BAILANGAN BULAT GANJIL/GENAP
print("Menentukan Bilangan Inputan User")

# INPUTAN DATA
angka = int(input("Masukan BIlangan: "))

# PROSES DATA
if angka == 0:
    print("Bilangan Nol")
else:
    if angka % 2 != 0:
     jenis ="ganjil"
    else:
     jenis ="genap"
    if angka > 0:
     sifat ="Positif"
    else:
     sifat ="Negatif"

#OUTPUT DATA
print(f"Bilangan {jenis} {sifat}")

# VERSI 2
angka = int(input("Masukan Bilangan: "))

# PROSES DATA
if angka == 0:
 print("Bilangan Adalah Nol")
elif angka % 2 != 0 and angka > 0:
 print("Bilangan Positif Dan Ganjil")
elif angka % 2 != 0 and angka < 0:
 print("Bilangan Negatif Dan Ganjil")
elif angka % 2 == 0 and angka > 0:
  print("Bilangan Positif Dan Genap")
else:
  print("Bilangan Negatif Dan Genap")
