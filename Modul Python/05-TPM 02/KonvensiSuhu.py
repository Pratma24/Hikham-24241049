# Meminta input dari pengguna dalam Fahrenheit
fahrenheit = float(input("Masukkan temperatur dalam Fahrenheit: "))

# Mengonversi Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Menampilkan hasil konversi
print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius:.2f} derajat Celsius.")