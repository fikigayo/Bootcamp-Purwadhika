use sakila;
#2
-- SELECT
--     f.rating,
--     AVG(f.rental_duration) AS avg_rental_duration
-- FROM film f
-- JOIN film_category fc ON f.film_id = fc.film_id
-- JOIN category c ON fc.category_id = c.category_id
-- GROUP BY 1
-- ORDER BY COUNT(f.film_id) DESC
-- LIMIT 3;

#3
WITH table_awal AS (
    SELECT film.title AS judul_film,
           COUNT(customer_id) AS total_penyewa
    FROM rental
    JOIN inventory ON inventory.inventory_id = rental.inventory_id
    JOIN film ON film.film_id = inventory.film_id
    GROUP BY 1
)
SELECT *
FROM table_awal
WHERE total_penyewa > (SELECT AVG(total_penyewa) FROM table_awal)
	AND total_penyewa BETWEEN 15 AND 25
ORDER BY 2 DESC