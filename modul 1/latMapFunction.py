# MAP dapat merubah data dari variable tersebut secara langsung
# [1,2,3,4] -> ['ganjil','genap','ganjil','genap']

list1 = [1,2,3,4,5]
def kali2(angka):
    return angka*2

hasilMap = map(kali2,list1)
print(hasilMap,type(hasilMap)) #ngecek tipenya

hasilMapList = list(hasilMap)
print(hasilMapList)

#pakai lambda
hasilMapLain = list(map(lambda angka :angka*2, list1))
print(hasilMapLain)
