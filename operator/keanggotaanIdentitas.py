a = [1, 2, 3, 4, 5]

# in (berada dalam) > objek yang sama dengan
1 in a  # true
"1" in a  # false

# not in (tidak berada dalam) > objek  yang berbeda dengan
"1" not in a  # true
4 not in a  # false

b = [1, 2, 3, 4, 5]
c = [1, 2, 3, 4, 5]
d = b

# operator is (biasanya untuk mengecek sumber suatu nilai)
b is b  # true
b is c  # false, padahal nilainya sama karena disimpan variabel/memori berbeda
b is d  # true, karena d mengambil nilai b (berada di memori yang sama)

# operator is not
b is not d  # false
