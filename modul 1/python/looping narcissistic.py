angka = int(input("Masukkan Angka: "))
pangkat = len(str(angka))  # Get the number of digits
total = 0
temp = angka

while temp > 0:
    digit = temp % 10
    total += digit ** pangkat
    temp //= 10

if total == angka:
    print(f"{angka} is a narcissistic number.")
else:
    print(f"{angka} isn't a narcissistic number.")
