# list []
# tuple ()
# set {}
# dictonary {key:value}
# string " "

# integer

# data yand ada di dalam tanda [ ] adalah data list

# data list
data_list = [1,2,0,4,5,6,7,8,9]
print(f"data list original : {data_list}")

# merubah data
print(f"data sebelum di ubah : {data_list}")
data_list[2] = 3
print(f"data setelah di ubah : {data_list}")

# meninsert data
data_list.insert(11,10)
print(f"insert data : {data_list}")

# cara mengambil data
index_0 = data_list[0]
print(f"index ke 0 adalah : {index_0}")
index_1 = data_list[1]
print(f"index ke 1 adalah : {index_1}")
index_2 = data_list[2]
print(f"index ke 2 adalah : {index_2}")
index_3 = data_list[3]
print(f"index ke 3 adalah : {index_3}")
index_4 = data_list[4]
print(f"index ke 4 adalah : {index_4}")
index_5 = data_list[5]
print(f"index ke 5 adalah : {index_5}")
index_6 = data_list[6]
print(f"index ke 6 adalah : {index_6}")
index_7 = data_list[7]
print(f"index ke 7 adalah : {index_7}")
index_8 = data_list[8]
print(f"index ke 8 adalah : {index_8}")
index_9 = data_list[9]
print(f"index ke 9 adalah : {index_9}")

# delete data
del data_list[2:5:6]
print(data_list)

# string
data_string = "kamu","bacot","sekali","kawan","delogok","kamu","yah"
data_baru = list(data_string)

print(f"data string : {data_baru}")