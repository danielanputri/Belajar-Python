#iterable > dapat diambil satu-persatu. berlaku untuk list, tuple, string, dict, etc
#for item(bebas varnya, bisa index atau i) in iterable(objek iterablenya):
    #kode yang akan dijalankan (dikasih)

var = [1,2,3]
for item in var:
    print(item)

var2 ="halo all"
for i in var2:
    print(f'huruf{i}')

var3 = [1,-2,3,-4,5,6,7,-8,-9,10,11,-12]

for index in var3:
    if index > 0:
        print(f'{index} adalah bilangan positif')
    else:
        print(f'{index} adalah bilangan negatif')
        
#contoh lainnya
jumlah = 2
for item in var3:
    jumlah += item
    print(jumlah)

#mencetak HEI sesuai dengan jumlah dalam var3
for _ in var3:
    print("HEI")

#tuple unpacking
varList = [(2,3), (3,4)]
for a,b in varList:
    print(a)
    print(b)

#dict unpacking
varDict = {1:"A", 2:"b"}
for item in varDict:
    print(item) #hanya mengambil key saja

for item in varDict.values:
    print(item) #hanya mengambil value saja

for (a,b) in varDict.items: #dijadikan tuple dulu buat print key and value
    print(f'key{a}') 
    print(f'value{b}')


#built in function 
#enumerate() print index dan elemennya
huruf = ["a", "b", "c"]

for i, item in enumerate(huruf):
    print(f'item ke-{i} adalah {item}')

#zip() menggabungkan 2 objek iterable
angka = [1,2,3]

for item in zip(huruf, angka):
    print(item) #hasilnya seperti tuple

for a,b in zip(huruf, angka):
    print(f'{a} dan {b}') #hasilnya digabung 

#range(start, end, step)
for i in range(5):
    print(i) #output ngeprint 0,1,2,3,4 

for i in range(2,5):
    print(i) #output ngeprint 2,3,4 

bilangan = []
for item in range(21):
    bilangan.append(item) #bilangan 0-20 menjadi elemen dalam list bilangan