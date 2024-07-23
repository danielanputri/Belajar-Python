# set menggunakan {}
# tipe data apa saja bisa masuk
a = {1, "dua", 3.3, 3, "b", "a"}  # kalau dirun hasilnya ga berurutan
# tidak dapat slicing dan indexing
# tidak berurutan
# mutable
# unik, tidak ada elemen yang sama, kalau ada yg sama otomatis ilang
satu = {1, 1, 2}  # output {1,2}

# set opration
# union: menggabungkan set dengan set
b = {1, 2, 3, 4}
c = {5, 2, 6, 4}
b.union(c)  # kalau ada yang sama ditulis sekali aja (123456)
b | c  # union

# intersection: menemukan elemen yang sama antar set
b.intersection(c)  # 2,4
b & c  # intersection

# difference: menemukan elemen yang ada pada set 1 tapi ga ada pada set 2
b.diffference(c)  # hasilnya 123 karena 123 ga ada pada c
b-c  # difference

# symmetric difference: menemukan elemen yang unik pada set 1 tapi ga ada pada set 2
b.symmetric_difference(c)  # hasilnya elemen yang sama ga ikut (1356)
b ^ c

# method
b.add(10)  # nambah 1 elemen
b.update(20, 30, 40)  # nambah banyak elemen sekaligus
b.remove(1)  # 1 hilang
set()  # konversi tipe data set

# built in function

# frozenset menggunakan {}
# tidak bisa tambah kurang elemen
# built in function frozenset() merubah menjadi frozen set
d = frozenset(b)  # mengubah b menjadi frozenset pada var d
