# class
# fungsi warna cookie
class cookie:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color

# input warna cookie
input_0 = input("masukan warna cookie satu : ")
input_1 = input("masukan warna cookie dua : ")

cookie_satu = cookie(input_0)
cookie_dua = cookie(input_1)

# hasil output
print("cookie satu adalah : ", cookie_satu.get_color())
print("cookie kedua adalah : ", cookie_dua.get_color())

# input ubah warna cookie
input_0 = input("warna cookie satu di ubah menjadi : ")
input_1 = input("warna cookie dua di ubah menjadi : ")

cookie_satu.set_color(input_0)
cookie_dua.set_color(input_1)

# hasil output ubah warna cookie
print("cookie satu setelah di ubah : ", cookie_satu.get_color())
print("cookie kedua setela di ubah : ", cookie_dua.get_color())