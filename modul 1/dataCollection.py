# numbers = [41, 5, 1, 3, 89, 32]
# min = min(numbers)
# max = max(numbers)


# buah = [
#     {"Nama": "Apel", "Stock": 10, "Harga": 10000},
#     {"Nama": "Jeruk", "Stock": 15, "Harga": 15000},
#     {"Nama": "Anggur", "Stock": 25, "Harga": 20000}
# ]

# while True:
#     menu = int(input("Masukkan angka Menu yang ingin dijalankan: "))
#     if menu == 1:
#         print("\nDaftar Buah:")
#         print("Index|Nama|Stock|Harga")
#         for i in range(len(buah)):
#             print(f"{i}|{buah[i]['Nama']}|{buah[i]['Stock']}|{buah[i]['Harga']}")
#     elif menu == 5:
#         print("\nExit Program")
#         break
#     else:
#         print("\nMenu tidak ada.")



# min = int(input("Masukkan jumlah minimal huruf: "))
# kalimat = input("Masukkan kalimat: ")

# kata = []
# for i in kalimat.split():
#     if(len(i)>=min):
#         kata.append(i)

# print(f"Kata-kata yang jumlahnya lebih dari {min} huruf adalah: {kata}")



# daftar_angka = input("Masukkan Angka dipisahkan dengan Spasi : ")
# list_awal = daftar_angka.split()
# list_ganjil = []
# for angka in list_awal:
#     if int(angka) % 2 == 1:
#         list_ganjil.append(angka)
# print("List Awal Adalah ",list_awal)
# print("Angka Ganjil dalam List Awal Adalah ",list_ganjil)



noHp = input("Masukkan nomor HP: ")

if len(noHp) > 13:
    print("Nomor HP yang dimasukkan berlebih")
else:
    if noHp.startswith("08"):
        print(f"Nomor telepon: {noHp}")
    else:
        print("Nomor HP harus dimulai dengan 08")