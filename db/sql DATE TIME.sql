#DATE #TIME #TIMESTAMP #DAY #DAYNAME(mon-sun) #MONTH #MONTHNAME(jan-dec) #YEAR
use sakila;
-- SELECT rental_id
-- 	,amount
--     ,payment_date
--     ,DATE(payment_date) AS date_payment
--     ,YEAR(payment_date) AS year_payment
--     ,MONTH(payment_date) AS month_payment
--     ,MONTHNAME(payment_date) AS month_name
--     ,DAY(payment_date) AS day_payment
--     ,DAYNAME(payment_date) AS day_name
--     ,DAYNAME(DATE(payment_date)+1) AS dayname_plus1
--     ,DAYOFMONTH(payment_date) AS dom_payment
--     ,DAYOFWEEK(payment_date) AS dow_payment
--     ,DAYOFYEAR(payment_date) AS doy_payment
--     ,WEEK(payment_date) AS week_payment
--  FROM payment LIMIT	10

SELECT YEAR(payment_date) AS year_payment
	, MONTH(payment_date) AS month_payment
	, MONTHNAME(payment_date) AS month_payment
    , SUM(amount) AS total_amount
FROM payment
GROUP BY 1,2,3
ORDER BY 1,2