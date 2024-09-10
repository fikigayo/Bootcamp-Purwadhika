-- SELECT column1 FROM TABLE_
-- WHERE column2 = (SELECT MAX(column2) FROM TABLE_)

-- select ID, SALARY,
-- (select AVG(SALARY) from employees)
-- AS Average_Salary
-- from employees;

-- select * from employees, salaries; FULL JOIN
-- select * from employees e, salaries s where e.emp_no = s.emp_no; ALIASES

-- 1. INNER JOIN -> Menggabungkan baris dari dua tabel berdasarkan kondisi yang sesuai di kedua tabel
-- 2. LEFT JOIN -> Menggabungkan semua baris dari tabel kiri dengan baris yang cocok dari tabel kanan, Jika tidak ada pasangan di tabel kanan, nilai NULL akan digunakan.
-- 3. RIGHT JOIN -> Kebalikan dari Left Join
-- 4. FULL JOIN -> Menggabungkan semua baris dari kedua tabel, Jika tidak ada pasangan di salah satu tabel, nilai NULL akan digunakan
-- 5. SELF JOIN -> Digunakan untuk menggabungkan baris dari tabel yang sama (tabel diri sendiri).