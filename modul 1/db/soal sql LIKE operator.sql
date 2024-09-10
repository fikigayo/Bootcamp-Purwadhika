#SELECT #FROM #WHERE #DISTINCT #COUNT #(AVG(),2) #LIMIT #ORDER BY 3(kolom ke 3)
#LIKE #BETWEEN #GROUP BY #HAVING #SUM #ROUND #LENGTH #UCASE #LCASE
# HAVING dipake kalau mau filter hasil dari agregat(avg sum count dsb)

#SELECT * FROM city WHERE district like 'y%a'
#SELECT * FROM city WHERE name like 'D___k'
#SELECT * FROM city WHERE population BETWEEN 1.5e4 AND 2e4

SELECT AVG(Population) AS Rata_rata, District AS Provinsi
FROM CITY WHERE CountryCode = 'IDN' GROUP BY District
HAVING Rata_rata > 5e5;