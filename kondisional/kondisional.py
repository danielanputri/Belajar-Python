#syntax if 
if 3>2:
    print ("benar") #pernyataan kondisi kalau true, kalau false tidak memunculkan apa-apa

#syntax if-elif
kondisi1 = True
kondisi2 = False

if kondisi1:
    print ("berhasil 1") #yang dijalankan ini, kalau 2 2 nya true maka yg dijalankan kondisi pertama
elif kondisi2:
    print ("berhasil 2") #kalau kondisi1 false, 2 true. maka yang dijalankan ini

x = 100
if x<0:
    print(f"{x} merupakan bilangan negatif")
elif x==0:
    print(f"{x} merupakan bilangan nol")

#Syntax if-else
kondisi = True
if kondisi:
    print("berhasil") #kalau true dijalankan ini
else:
    print("tidak berhasil") #kalau false dijalankan ini

x = -1
if x<0:
    print(f"{x} merupakan bilangan negatif")
else:
    print(f"{x} merupakan bukan bilangan negatif")

#Syntax if-elif-else
kondisi1 = False
kondisi2 = True
if kondisi1:
    print("berhasil") #kalau true dijalankan ini
elif kondisi2:
    print("berhasil 2") #kalau true dijalankan ini, berlaku kondisi 1 false
else:
    print("tidak berhasil") #kalau false keduanya dijalankan ini

x = 2
if x>0:
    print(f"{x} merupakan bilangan positif")
elif x==0:
    print(f"{x} merupakan bilangan nol")
else:
    print(f"{x} merupakan bilangan negatif")

#pernyataan if di dalam if
x = 2
if x>0:
    print(f"{x} merupakan bilangan positif")
    if x<10:
        print(f"{x} merupakan bilangan positif antara 0-10") #kalau ini true, yg diprint 2 sama atasnya. bisa tambah else juga
elif x==0:
    print(f"{x} merupakan bilangan nol")
else:
    print(f"{x} merupakan bilangan negatif")

#conditional expression dari if else
kondisi = True
if kondisi:
    print("berhasil") #kalau true dijalankan ini
else:
    print("tidak berhasil") #kalau false dijalankan ini
#lebih ringkas dan singkat
print("berhasil") if kondisi else print("tidak berhasil")