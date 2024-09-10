#Tuple = list yang tidak bisa diubah
tupleContoh = ('hello',1,2,3,True,('red pen','blue pen'))
print(tupleContoh[-1:])

# tupleContoh[0] = 'ga bisa diubah karna tuple'
#ngakali
tupleList = list(tupleContoh)
tupleList[0] = 'ganti'
print(tupleList)

#ngecek
print('hellop' in tupleContoh)

# print(tupleContoh + tupleList) TUPLE TIDAK BISA DIGABUNG DENGAN LIST BIASA

print(tupleContoh.index('hello')) #cek dia index ke berapa