use world;
#SELECT SUM(Population) AS total_populasi FROM country where region = 'Southeast Asia';

#select * from country limit 10;

#SELECT AVG(GNP) AS Average_GNP FROM country where region = 'Eastern Africa';

#SELECT AVG(Population) FROM country WHERE SurfaceArea > 5000000;

#SELECT Name, SurfaceArea FROM country where SurfaceArea > 1200000 and continent = 'Africa';

#SELECT * FROM country WHERE GovernmentForm= 'Republic' AND Continent = 'Asia';

SELECT * FROM country WHERE continent = 'Asia' AND population > 1e8;