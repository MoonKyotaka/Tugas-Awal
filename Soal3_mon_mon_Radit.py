#

angka = int(input("Masukkan bilangan: "))

#PROSES DATA
deret = []
jumlah_total = 0
jumlah_genap = 0
for i in range(1, angka + 1):
    deret.append(i)
    jumlah_total += i
    if i % 2 == 0:
     jumlah_genap += i

#OUTPUT DATA
print(f"Deret bilangan: {deret}")
print(f"Jumlah total bilangan: {jumlah_total}")
print(f"Jumlah bilangan genap: {jumlah_genap}")