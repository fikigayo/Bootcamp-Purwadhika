use world;
-- SELECT COUNT(DISTINCT(region)) FROM country;
-- SELECT COUNT(name) FROM country WHERE continent = 'Africa'
-- SELECT Name, Population FROM country ORDER BY 2 DESC LIMIT 5
-- SELECT AVG(GNP) FROM country WHERE continent = 'Africa'

-- SELECT Region, COUNT(Region) AS Total_Region
-- FROM country WHERE continent = 'Africa' 
-- GROUP BY 1 HAVING Total_Region > 3;

-- SELECT Continent, AVG(LifeExpectancy) AS Avg_Life_Exp FROM country
-- GROUP BY 1 ORDER BY 2

-- SELECT Region, AVG(GNP) AS avg_gnp FROM country WHERE continent = 'Africa'
-- GROUP BY 1 ORDER BY 2 DESC

-- SELECT Name FROM country WHERE continent = 'Europe' 
-- AND Name LIKE 'I%'

-- SELECT COUNT(DISTINCT(Language)) FROM countrylanguage;

-- SELECT Name FROM country WHERE LENGTH(Name) = 6 AND Name LIKE '%o'

-- SELECT * FROM countrylanguage WHERE CountryCode = 'IDN' 
-- ORDER BY 4 DESC LIMIT 7

SELECT * FROM country WHERE IndepYear IS NOT NULL ORDER BY IndepYear LIMIT 10