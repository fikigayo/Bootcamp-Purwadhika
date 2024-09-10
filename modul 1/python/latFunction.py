#regular function
def tambah(angka1,angka2):
    return angka1+angka2

hasil = tambah(1,2)
print(hasil)

#lambda function
lambda angka1,angka2 : angka1 + angka2

#function parameter kosong
def salam():
    print('halo')
salam()

#function with input and no output
def salamBalik(nama,usia):
    print(f'halo nama saya {nama}, umur saya {usia}')

salamBalik('fiki',27)

# bisa gini juga buat kasi default parameter
# def salamBalik(nama = 'fiki',usia = 27):
#     print(f'halo nama saya {nama}, umur saya {usia}')

# (LOCAL VARIABLE) tidak bisa diakses diluar function
def filterGanjil(listAngka):
    ganjil = []
    for angka in listAngka:
        if angka%2==0:
            ganjil.append(angka)
    return ganjil

list1 = [1,2,3,4,5,6,7,8,9,10]
ganjil1 = filterGanjil(list1)
print(ganjil1)


#(GLOBAL VARIABLE) variable yang bisa diakses di seluruh function
def coba():
    global x #ambil variable diluar function x = 5
    x += 8
    print(x+2)
    return x+3
x = 5
print(coba(),x)

#function dalam function (callback)
def tambah(num1,num2):
    return num1+num2
def kurang(num1,num2):
    return num1-num2

def total(fn,angka1,angka2):
    return fn(angka1,angka2)

print(total(tambah,10,3))
print(total(kurang,10,3))

#rekursif
def countdown(count):
    print(count)
    count -=1
    if count >= 0:
        countdown(count) #dipanggil lagi function nya hingga angkanya 0

countdown(10)