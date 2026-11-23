#MEMBUAT KODE PROGRAM KOVERSI ANGKA MENJADI HURUF

#PERSAYARTAN PROGRAM DAN INPUTAN DATA
while True:
    try:
        angka = int(input("Masukan Angka (1-100): "))
        if 0 <= angka <= 100:
            break
        else:
         print("**Angka tidak valid Mohoon Masukan Angka dari 0 sampai 100**")
    except ValueError:
         print("**Mohon Masukan Angka Bukan Huruf !!**")

#PROSES DATA 
if angka >= 85:
   huruf ="A" 
elif angka >= 75:
   huruf ="B"  
elif angka >= 55:
   huruf ="C"  
elif angka >= 40:
   huruf ="D"  
else:
   huruf ="E"

print(f"Grade : {huruf}")

#VERSI LAIN NYA

angka = int(input("Mohon Masukan Angka Yang Valid (1-100): "))

#PROSES DATA
if angka < 0 or angka > 100:
   print()


    
        
  