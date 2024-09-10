harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000
apel, jeruk, anggur =  int(input('masukan apel:')), int(input('masukan jeruk:')), int(input('masukan anggur:'))
total_harga = harga_apel*apel+harga_anggur*anggur+harga_jeruk*jeruk
print(f'Detil belanja\n Apel: {harga_apel*apel}\n jeruk {harga_jeruk*jeruk}\n anggur {harga_anggur*anggur}\n total: {total_harga}')
uang_anda = int(input('masukan uang anda:'))
i = f'Transaksi dibatalkan uangnya kurang sebesar {total_harga-uang_anda}' if total_harga-uang_anda > 0 else ( f'Transaksi dibatalkan uangnya kurang sebesar {uang_anda-total_harga}' if total_harga-uang_anda < 0 else 'Terimakasih' )
print(i)