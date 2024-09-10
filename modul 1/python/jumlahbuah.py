x = 485
tahun = x//360
sisaHari = x%360
bulan = sisaHari//30
hari = bulan%30
print(f'{tahun} Tahun {bulan} Bulan {hari} Hari')