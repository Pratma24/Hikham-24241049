# Casting
# mengubah tipe data ke tipe data lain
# tipe data = int,float,str,bool

## INTEGER
print("===INTEGER===")
data_int = 9 
print("data : ", data_int, "type = ", type(data_int))

# ubah integer ke float 
data_float = float(data_int)
# ubah integer ke string
data_str = str(data_int)
# ubah integer ke boolean 
data_bool = bool(data_int)
# cetak
print("data : ", data_float, "type = ", type(data_float))
print("data : ", data_str, "type = ", type(data_str))
print("data : ", data_bool, "type = ", type(data_bool))

## FLOAT
print("===FLOAT===")
data_float = 3.14
print("data : ", data_float, "type = ", type(data_float))

# ubah menjadi integer
data_int = int(data_float)
# ubah menjadi boolean
data_bool = bool(data_float)
# ubah menjadi string
data_str = str(data_float)

#cetak
print("data : ", data_int, "type = ", type(data_int))
print("data : ", data_str, "type = ", type(data_str))
print("data : ", data_bool, "type = ", type(data_bool))