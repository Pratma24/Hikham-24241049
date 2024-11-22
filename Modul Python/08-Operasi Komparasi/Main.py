# Operasi komparasi

# Setiap hasil dari komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# Lebih besar dari >
print("================== lebih dari (>)")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Kurang dari <
print("================== lebih dari (<)")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih dari sama dengan >=
print("================== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Kurang dari sama dengan <=
print("================== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama dengan (==)
print("================== sama dengan (==)")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak sama dengan (!=)
print("================== sama dengan (!=)")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# "is" sebagai komparasi objek indentity
print("================== objek identity (is)")
x = 5 # ini adalah assignment membuat objek
y = 5
print("nilai x =",x,",id = ",hex(id(x)))
print("nilai y =",y,",id = ",hex(id(y)))
hasil = x is y
print("x is y",hasil)

x = 5 # ini adalah assignment membuat objek
y = 6
print("nilai x =",x,",id = ",hex(id(x)))
print("nilai y =",y,",id = ",hex(id(y)))
hasil = x is y
print("x is y",hasil)

print("================== objek identity (is not)")
x = 5 # ini adalah assignment membuat objek
y = 6
print("nilai x =",x,",id = ",hex(id(x)))
print("nilai y =",y,",id = ",hex(id(y)))
hasil = x is not y
print("x is not y",hasil)

x = 5 # ini adalah assignment membuat objek
y = 5
print("nilai x =",x,",id = ",hex(id(x)))
print("nilai y =",y,",id = ",hex(id(y)))
hasil = x is not y
print("x is not y",hasil)