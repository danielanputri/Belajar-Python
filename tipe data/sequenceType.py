# list (seperti array [])
nama = ["budi", "miaw"]
daftar = ["budi", 1]

# list index dari 0, kalau -1 berarti ambil angka dari belakang
a = [1, 2, 3]
a[:1]  # dari awal sampe index 1. 0
a[:2]  # dari awal sampe index 2. 0 1

# list mutable
a[0] = "satu"  # var a akan berubah "satu"

# concanetanion (gabungin list)
b = [4, 5, 6]
a+b  # listnya jadi 1

# repetition # mengalikan list dengan integer
b*3  # menghasilkan list berulang 3x

# method
a.append(7)  # ada elemen baru paling belakang
a.sort()  # ngurutin dari  kecil terbesar
a.sort(reverse=True)  # besar ke kecil
a.reverse()  # besar ke kecil
a.clear()  # menghapus semua list
b.pop(2)  # menghapus elemen index kedua

# build in function
# list() konversi tipe data menjadi list
c = (1, 2)
list(c)
sapa = "hai"
list(sapa)

# max() min() mengambil tipe data maksimal minimal
min(b)
max(b)

# lainnya
type(b)
len(b)
print(b)

# tuple (seperti function, pakai ())
z = (1, 2, 3, 4, 5)
x = (1, 2, "tiga", [4])
v = (1, (2, 3), 4)

# index dan slicing sama ky list
# tupple immutable
# concatenation dan multiplication sama ky list

# method()
z.count(1)  # menghitung elemen 1 pada z
z.index(1)  # mencari index 1 ada dimana, kalau ada double milih yang pertama ditemui

# build in function
tuple(b)  # konversi tipe data ke tuple
# lainnya sama ky list
