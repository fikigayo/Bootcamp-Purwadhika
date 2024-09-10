
# for i in range(5, 0, -1):
#     print('*' * i)

# for i in range(2, 6):
#     print('*' * i)


# Soal 2
# for i in range(1, 50):
#     if i % 3 == 0:
#         print(i)

#Soal 1

# kalimat = 'Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat in'
# kata = kalimat.split()
# for i in kata:
#     if 'K' in i or 'k' in i:
#         print(i)

# kalimat = 'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'
# for i in kalimat.split():
#     if len(i) % 2 == 0:
#         print(i)

# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} adalah kelipatan 3 dan 5')
#     elif i % 3 == 0:
#         print(f'{i} adalah kelipatan 3')
#     elif i % 5 == 0:
#         print(f'{i} adalah kelipatan 5')
#     else:
#         print(i)


# x = int(input("Masukkan jumlah baris maksimal: "))
# for i in range(1, x+1):
#     for j in range(1, i+1):
#         print(j,end='')
#     print('')

# last = int(input("Masukkan angka terakhir yang ditampilkan: "))
# x1 = int(input("Masukkan bilangan 1: "))
# x2 = int(input("Masukkan bilangan 2: "))

# for i in range(1, last + 1):
#     if i % x1 == 0 and i % x2 == 0:
#         print("fizzbuzz")
#     elif i % x2 == 0:
#         print("buzz")
#     else:
#         print(i)

# kalimat = input("Masukkan Sebuah kata/kalimat: ")

# jlh_huruf = 0
# jlh_angka = 0

# for karakter in kalimat:
#     if karakter.isalpha():
#         jlh_huruf +=1
#     elif karakter.isdigit():
#         jlh_angka +=1

# print(f'Jumlah Huruf Pada Kalimat Sebanyak {jlh_huruf}')
# print(f'Jumlah Angka Pada Kalimat Sebanyak {jlh_angka}')


input = int(input("Masukkan Angka: "))
digits = len(str(input))
total = 0
temp = input
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if total == input:
    print(f"{input} is a narcissistic number.")
else:
    print(f"{input} isn't a narcissistic number.")