#fungsinysa sama kaya map
#hanya saja difilter mengurangi/menambah data berdasarkan function yang diberikan
def mapDuplikat(fn,collection):
    newCollection = []
    for item in collection:
        newCollection.append(fn(item))
    return newCollection

def ubahAngka(angka):
    return f'Angka {angka}'

list1 = [1,2,3,4,5]

newList = mapDuplikat(ubahAngka,list1)
print(newList)

#CONTOH 2 filter genap
def angkaGenap(angka):
    return angka %2 ==0

hasilFilter = list(filter(angkaGenap, list1))
print(hasilFilter)

#pakai lambda
print(list(filter(lambda x:x%2==0,list1)))