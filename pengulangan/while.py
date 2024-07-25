#while > menjalankan kode selama hasilnya true, kalau false maka berhenti

x = 5
while x>0: #pengkondisian
    print("hei")
    x -= 1 #x berkurang 1  jika terjadi pengulangan
#hati-hati kalau tidak dikasih perbandingan loop tidak berhenti (solve: interrupt or restart kernel)

x = 5
while x>0: 
    print("hei")
    x -= 1
else:
    print("selesai")

#loop control statement 
# 1. pass > tidak melakukan apapun
var = [1,2,3,4,5]
for  i in var:
    if i == 2: #tidak menampilkan angka 2 di var dengan pass
        pass #kosong
    else:
        print(i)

# 2. continue > tidak menjalankan kode dibawahnya dan melanjutkan perulangan
var = [1,2,3,4,5]
for  i in var:
    if i == 2: #i  bernilai true saat 2 makanya continue, kode dibawahnya tidak dieksekusi (skip)
        continue ##tidak menampilkan angka 2 di var dengan continue
        print(i)

# 3. break > menghentikan perulangan
var = [1,2,3,4,5]
for  i in var:
    if i == 2: #i  bernilai true saat 2 makanya break, loopingnya berhenti
        break #berhenti
        print(i) #output 1

x = 5
while True: 
    print("hei")
    x -= 1
    if x == 0:
        break