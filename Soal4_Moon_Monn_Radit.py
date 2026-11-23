#PROGMAN

#PROSES DATA
n = int(input("Masukkan N: "))
print("\n-_-Segitiga Siku Siku-_-")

for i in range(1, n + 1):
    print("*" * i)

print("-_-Segitiga Siku Siku Terbalik-_-")
for i in range(n, 0, -1):
    print("*" * i)