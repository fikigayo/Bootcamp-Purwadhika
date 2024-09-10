# passenger = [[90,0],[25,30],[50,20],[10,30]]
# masuk = 0
# keluar = 0
# sisa = 0
# for i in passenger:
#     if(sisa+i[0]-i[1]>100):
#         sisa = 100
#     else:
#         sisa += i[0]
#         sisa -= i[1]
# print(sisa)


ip1 = input("IP pertama: ").split('.')
ip2 = input("IP kedua: ").split('.')

value1 = int(ip1[0]) * 256**3 + int(ip1[1]) * 256**2 + int(ip1[2]) * 256 + int(ip1[3])
value2 = int(ip2[0]) * 256**3 + int(ip2[1]) * 256**2 + int(ip2[2]) * 256 + int(ip2[3])


result = abs(value1 - value2)
print(result)