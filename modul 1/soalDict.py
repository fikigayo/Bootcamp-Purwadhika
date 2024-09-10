# str = input('masukkan string: ')
# find = input('masukkan yang dicari: ')
# jlh = str.count(find)
# print(f"{find} muncul {jlh} kali dalam string.")


tumpukan = input("Masukkan string: ")
jarum = []
index = len(tumpukan)
for i in range(index):
    if tumpukan[i] == '|':
        jarum.append(str(i)) #dimasukin ke string dulu biar bisa di join nantinya
print(', '.join(jarum))

# str = input('Masukkan string: ')

# o = str.count('o')
# x = str.count('x')
# if o == x:
#     print('Balanced')
# else:
#     print('Not Balanced')