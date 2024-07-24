# dictionary(dict) seperti set, dengan 2 jenis key value dipisahkan :
# key unik value muttable, dict bersifat mutable, heterogen: bisa berbeda-beda tipe datanya
{1: "a", 2: [2, 3, 4], 3: (1, 2, 3)}
dataKaryawan = {"nama": ["vemas", "yela"], "umur": [20, 19]}
dataKaryawan["nama"]  # akses nama

a = {1: "b"}
a[1] = "c"  # berubah jadi c

# method
dataKaryawan.get("nama")  # manggil nama
dataKaryawan.keys()  # key dari data karyawan dict[key] dict.get(key)
dataKaryawan.values()  # values dari data karyawan berupa list

# built in function
c = dict()  # ga ada isinya
c[1] = 'a'  # key 1 value a
