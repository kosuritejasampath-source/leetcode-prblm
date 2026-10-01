/* Write your PL/SQL query statement below */
SELECT e.name AS employee
FROM
employee e
JOIN 
employee m
ON e.managerId=m.id
WHERE e.salary>m.salary;