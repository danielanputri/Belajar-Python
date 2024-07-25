#membuat list lebih singkat menggunakan loop
#[ekpresi for item in iterable if kondisi]

var = 'selamat'
listVar = [i for i in var ] #setiap karakter selamat menjadi elemen dalam var

var1 = [1,2,3]
list_var =  [item*2 for item in var] #membuat list dari var1 namun bilangannya dikali 2
#output [2,4,6]

angka = [i for i in range(1,11)]
angka #output variabel angka (list) 1 - 10

genap = [i for i in range(2,21,2)] #dimulai 2, sampe kurang 21, step/loncat 2
genap #output variabel angka genap (list) 2 - 20

#menambahkan pernyataan kondisional
ganjil = [i for i in range(1,21) if i%2 == 1]
ganjil #output variabel angka ganjil (list) 1 - 21

salam = 'selamat'
listSalam = [i for i in salam if i == 'a' ] 
listSalam #hanya mengambil karakter a pada selamat

stringGanjil = ["Ganjil" if i%2 == 1 else i for i in range(1,21)]
stringGanjil #output angka ganjil menjadi string "Ganjil"

#Multivariabel
varA = [1,2,3]
varB = [10,20,30]

varC= [x*y for x in varA for y in varB]
varC #output perkalian masing-masing elemen varA dan varB
#[10,20,30,20,40,60,30,60,90]