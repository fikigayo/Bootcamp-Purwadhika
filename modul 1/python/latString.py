str1 = "halo nama saya \"Fiki\""
str2 = 'halo nama saya "Fiki"'
str3 = '''halo nama saya "Fiki"'''
str4 = "halo nama saya 'Fiki'"
str5 = "halo nama saya \n'Fiki'"
str6 = "halo nama saya \t\t\t\t'Fiki'"
str7 = 'hello i\'m fiki'
str8 = 'hello kontrrr\b\b\bol!' #hapus huruf sebelumnya 
str9 = 'backslash \\\\' #tampilin backslash dengan backslash
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)
print(str9)

str1 = 'Halo apa Kabar'
xIndex = str1.index('apa') #type nya int
print(xIndex)

xSplit = str1.split(' ') #type nya array
print(xSplit)

xlow = str1.lower() #lowercase
print(xlow)

xupper = str1.upper() #upper case
print(xupper)

xcapital = str1.capitalize() #capitalize
print(xcapital)

#-------String Slicing-------
text = "I'm Baron, nice to meet you"
print(text[1])          # ' (string ke 1)
print(text[2:])         # m Baron, nice to meet you (setelah index 2)
print(text[:4])         # I'm  (sebelum index 4)
print(text[2:5])        # m B  (Range index 2 hingga 5)
print(text[:])          # I'm Baron, nice to meet you (semua)
print(text[-1])         # u (string terakhir ke 1)
print(text[-3:])        # you (string dari 3 huruf terakhir)
print(text[:-5])        # I'm Baron, nice to mee (string sebelum 3 huruf terakhir)
print(text[3:-1])       #  Baron, nice to meet yo

text = "Skill accelerator bootcamp"
print(text[2:-2])