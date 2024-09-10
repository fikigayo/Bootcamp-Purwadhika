SELECT
    c.name AS category_name,
    SUM(f.rental_duration) AS total_rental_duration,
    SUM(SUM(f.rental_duration)) OVER (ORDER BY SUM(f.rental_duration) DESC) AS cumulative_sum,
    AVG(SUM(f.rental_duration)) OVER (ORDER BY SUM(f.rental_duration) DESC) AS moving_avg_duration
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE f.rental_duration <= (SELECT AVG(rental_duration) FROM film)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;