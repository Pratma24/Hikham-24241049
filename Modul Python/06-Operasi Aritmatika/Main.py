# Operasi Aritmatika

a = 10
b = 3

# Operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# Operasi pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# Operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# Operasi pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# Operasi modulus (sisa bagi) %
hasil = a % b
print(a,"%",b,"=",hasil)

# Operasi floor division (pembulatan) //
hasil = a // b
print(a,"//",b,"=",hasil)

# Prioritas operasi, Operational precedence
'''
  1. ()
  2. exponen **
  3. perkalian dan kawannya  * / ** % //
  4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,hasil)


hasil = x + y * z
print(x,"+",y ,"*", z,"=",hasil)
# kurung akan menganbil langkah paling pertama
hasil = (x + y) * z
print("(",x,"+",y,") *",z,"=",hasil)