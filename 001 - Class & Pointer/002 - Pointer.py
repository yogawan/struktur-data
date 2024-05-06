# pointer
input = int(input("masukan angka : "))
num_satu = input
num_dua = num_satu

print("sebelum num_two telah di update : ")
print("num satu :", num_satu)
print("num dua :", num_dua)

print("nilai num satu :", id(num_satu))
print("nilai num dua :", id(num_dua))

# kalkulator sederhana
setBilangan_satu = int(input("masukan angka : "))
operator = input("operator (+,**) : ")
setBilangan_dua = int(input("masukan angka : "))

if operator == "+":
    hasil = setBilangan_satu + setBilangan_dua
    print(f"hasil penjumplahan : {hasil}")
if operator == "**":
    hasil = setBilangan_satu ** setBilangan_dua
    print(f"hasil penjumplahan : {hasil}")
else:
    print("tidak bisa menjumplahkan angka karena tidak ada operator operasi, operator yang tersedia (+,-,x,/)")