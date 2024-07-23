# string pakai petik "heelo" 'string'
# index dimulai dari 0, -1 dari belakang (dikurangi kata -1 tsb). bisa buat slicing juga.
string = "Python"
# index tidak dapat diubah

var = "Python Keren"
var[0]  # 'P'
var[-1]  # n

# slicing [starts:stop:step]
var[0:2]  # Py ngambil indeks 0 dan 1, 2 ga ikut.
var[2:6]  # thon
var[2:]  # thon Keren
var[:6]  # Python
var[:6:2]  # Pto --> loncat 2x
var[:6:3]  # Ph --> loncat 3x
var[:]  # Python Keren
var[::-1]  # baca dari belakang, nereK nohtyP

# Concatenation
var2 = "Hai"
var2 + "Daniela"

# Multiplication
var2*2

# String Method
nama = "daniela"
nama.capitalize()  # Awal kalimat menjadi kapital
nama.upper()  # semua kalimat menjadi kapital
nama.lower()  # semua kalimat menjadi kecil
nama.strip()  # mwnghapus spasi kosong di depan atau belakang string

# Built in function len(), menghitung panjang string
len("halo")  # 4

# print() nampilin objek atau print/cetak objek
print("Halo Dunia")
# \n membuat baris baru
print("Halo \nDunia")
# \t mewakili tab
print("Halo \tDunia")
# \' \" mewakili petik

# String formatting .format, f-string, (%s %r)
name = "yella"
nilai = "99.56734567"
print("nama dia adalah %s" % (nama))
print("nama dia adalah %r" % (nama))  # jadi 'yella'
print("nilai dia adalah %d" % (nilai))  # %d untuk integer, kecetak 99
print("%s mendapatkan nilai %d" % (nama, nilai))  # gabung
# .3 berarti 3 dibelakang koma. 1 berarti di depannya lebih lebar?
print("nilai dia adalah %1.3f" % (nilai))

# .format()
nilai_andi = 50
nilai_ani = 70
print("nilai ulangan andi {} sedangkan ani {}".format(nilai_andi, nilai_ani))
# index
print("nilai ulangan andi {1} sedangkan ani {0}".format(
    nilai_andi, nilai_ani))  # nilainya ketuker
# menggunakan keyword
print("nilai ulangan andi {a} sedangkan ani {b}".format(
    a=nilai_andi, b=nilai_ani))
# f-string
print(f'{nama} memiliki nilai {nilai}')
# float
print(f'{nama} memiliki nilai {nilai:3.3f}')
