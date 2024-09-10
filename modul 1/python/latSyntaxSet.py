#set penyimpanan yang tidak punya index
#tidak ada data duplikat

##set contoh
set1 = {'The Avengers','Ironman 3', 'Spiderman', 'Ironman 3'}
# print(set1) #Ironman 3 hanya muncul 1 karna duplikat
# for item in set1:
#     print(item)

# print('Ironman 3' in set1) #cek film ada di list

# --- menambah data ---
set1.add('Batman')

# --- menambah data lebih dari 1 ---
set1.update({'Hulk','Batman'})

# --- menghapus data set ---
set1.remove('Ironman 3') # bisa pakai .remove atau .discard
print(set1)

# --- hapus semua ---
# set1.clear()

set2 = {'Captain Marvel', 'Antman'}

# --- menggabungkan set dengan set lain ---
print(set1.union(set2)) # menggunakan .union

# --- irisan dari set ---
print(set1.symmetric_difference(set2))




#membuat set dari list, tuple dan dictionary1, dictionary
list1 = ['budi', 2,2,'ceci']
tuple1 = (False,1,'andi',True)
dict1 = {'nama':'fiki', 'usia':27, 'pekerjaan':'coder','menikah':True}

# set_list = set(list1)
# set_tuple = set(tuple1)
# set_dict = set(dict1)
# set_dict_val = set(dict1.values())
# print(set_list)
# print(set_tuple)
# print(set_dict)
# print(set_dict_val)



# film1 = set(input("Masukkan 5 Film Kesukaan anda: ").split(','))
# film2 = set(input("Masukkan 5 Film Kesukaan teman: ").split(','))

# if((len(film1) and len(film2))== 5):
#     persen = (len(film1 & film2)/5)*100
#     print(f"Kesukaan Film kalian yang sama sebesar {persen}%")
# else:
#     print(f'Masukkan masing-masing 5 Film')

# film1 = set(input("Masukkan Film Kesukaan anda: ").split(','))
# film2 = set(input("Masukkan Film Kesukaan teman: ").split(','))
# total = 0
# for i in film1:
#     for j in film2:
#         if i == j:
#             total +=1
# persen = total/5*100
# print(f"Kesukaan Film kita sebesar {persen}%")