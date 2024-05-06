def bubble_sort(my_list):
    print(my_list,'\n')
    for i in range(len(my_list) - 1, 0 ,-1):
        print('langkah',i)
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
            print(my_list,'\n')
    return my_list

print('\n',bubble_sort([4,2,6,5,1,3]))