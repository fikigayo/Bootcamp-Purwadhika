# Dictionary
# -variable yang memiliki banyak data
# -index nya berupa text

dictionaryContoh = {
    'nama' : 'Budi',
    'usia' : 25,
    'pekerjaan' : 'Developer',
    'menikah' : False,
}
dictionaryContoh2 = dict(
    nama = 'Budi',
    usia = 25,
    pekerjaan = 'Developer',
    menikah = False,)

#cara akses
print(dictionaryContoh['nama'])
print(dictionaryContoh2['pekerjaan'])

#ganti data
dictionaryContoh2['usia'] = 27
print(dictionaryContoh2['usia'])

#nambah data
dictionaryContoh2['agama'] = 'islam'
print(dictionaryContoh2['agama'])

#delete data
del dictionaryContoh2['agama']
# dictionaryContoh2.pop('agama')
# dictionaryContoh2.popitem() #hapus data terakhir

#hapus semua
# dictionaryContoh2.clear()

#dictionari dalam dictionary
toko = ({
    'ssd' : {
        'samsung' : 1000000,
        'adata' : 800000,
    },
    'prosessor' : {
        'intel' : 3000000,
        'amd' : 2000000,
    }
})

print(toko['ssd'])

# looping
for k in toko:
    print(f'jenis nya adalah {k}, merk nya adalah {toko[k]}')

# looping value nya aja cth harganya
# for k in toko.values():

#ambil key dan value nya
for k,v in toko.items():
    print(f'key nya adalah {k}, valuenya adalah {v}')

# cek apakah ada di dictionary
print('samsung' in toko['ssd'])


#cek panjang dict
print(len(toko['ssd']))

copiedToko = toko.copy()
copiedToko['ssd']['samsung'] = 123456

print(toko['ssd']['samsung'])
print(copiedToko['ssd']['samsung'])

# dictionary with tupple JSON
dictWithTuple ={
    'name' : ['asep','budi'],
    'umur' : [25,37],
    'pekerjaan' : ['dev'],
}

# dictionary with tupple V2
dictWithTuple ={
    'name' : ('asep','budi'),
    'umur' : (25,37),
    'pekerjaan' : ('dev','programmer'),
}