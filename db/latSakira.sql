use sakila;

-- SELECT first_name FROM actor WHERE first_name LIKE '%Scarlet%';
-- SELECT COUNT(DISTINCT(last_name)) FROM actor;
-- SELECT last_name FROM actor GROUP BY 1 HAVING COUNT(last_name) = 1 ORDER BY 1 LIMIT 5
-- SELECT last_name FROM actor GROUP BY 1 HAVING COUNT(last_name) > 1 ORDER BY 1 LIMIT 5
-- SELECT AVG(length) AS rata_rata_durasi FROM film;

-- SELECT customer.* FROM customer 
-- JOIN address ON customer.address_id = address.address_id
-- JOIN city ON city.city_id = address.city_id
-- JOIN country ON country.country_id = city.country_id
-- WHERE country = 'Indonesia' AND phone % 2 = 1
-- ORDER BY postal_code,customer_id

-- SELECT MONTHNAME(payment_date) AS bulan ,AVG(amount) AS rata_rata_amount
-- FROM payment GROUP BY 1	ORDER BY 2 DESC
