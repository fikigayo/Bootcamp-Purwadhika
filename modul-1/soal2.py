i = float(input())
y = float(input())
x = i/y**2
if x<18.5:
    print('berat badan kurang')
elif x<25:
    print('berat badan ideal')
elif x<30:
    print('berat badan berlebih')
elif x<40:
    print('berat badan sangat berlebih')
else:
    print('berat badan obesitas')