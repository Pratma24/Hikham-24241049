# Meminta input dari pengguna
angka = int(input("Masukkan sebuah bilangan: "))

# Menggunakan operator modulus untuk menentukan ganjil atau genap
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap.")
else:
    print(f"{angka} adalah bilangan ganjil.")