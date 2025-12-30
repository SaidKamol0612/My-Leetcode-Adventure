# SQL 50

---

## Select

### Problem: 1

**1757. Recyclable and Low Fat Products**

```sql
-- Solution
SELECT product_id FROM Products
WHERE low_fats = 'Y' and recyclable = 'Y';
```

### Problem: 2

**584. Find Customer Referee**

```sql
-- Solution
SELECT name FROM Customer
WHERE referee_id is null or referee_id != 2;
```

### Problem: 3

**595. Big Countries**

```sql
-- Solution
SELECT name, population, area FROM World
WHERE area >= 3000000 or population >= 25000000;
```

### Problem: 4

**1148. Article Views I**

```sql
-- Solution
SELECT DISTINCT author_id as id FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;
```

### Problem: 5

**1683. Invalid Tweets**

```sql
-- Solution
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;
```

---

# Basic Joins

### Problem: 6

**1378. Replace Employee ID With The Unique Identifier**

```sql
-- Solution
SELECT u.unique_id, e.name FROM Employees e
LEFT JOIN EmployeeUNI u ON u.id = e.id;
```

### Problem: 7

**1068. Product Sales Analysis I**

```sql
-- Solution
SELECT p.product_name, s.year, s.price FROM Product p
RIGHT JOIN Sales s ON s.product_id = p.product_id;
```

### Problem: 8

**1581. Customer Who Visited but Did Not Make Any Transactions**

```sql
-- Solution
SELECT v.customer_id,
   COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;
```

### Problem: 9

**197. Rising Temperature**

```sql
-- Solution
SELECT w2.id FROM Weather w1
RIGHT JOIN Weather w2 ON TIMESTAMPDIFF(DAY, w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature < w2.temperature;
```

### Problem: 10

**1661. Average Time of Process per Machine**

```sql
-- Solution
SELECT
a1.machine_id,
ROUND(AVG(a2.timestamp - a1.timestamp), 3) as processing_time
FROM Activity a1
INNER JOIN Activity a2
ON a1.machine_id = a2.machine_id
and a1.process_id = a2.process_id
and a1.activity_type = 'start'
and a2.activity_type = 'end'
GROUP BY a1.machine_id;
```

### Problem: 11

**577. Employee Bonus**

```sql
-- Solution
SELECT e.name, b.bonus FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 or b.bonus is NULL;
```

### Problem: 12

**1280. Students and Examinations**

```sql
-- Solution
SELECT
     s.student_id,
     s.student_name,
     sub.subject_name,
      COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
      ON s.student_id = e.student_id
      AND sub.subject_name = e.subject_name
GROUP BY s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
```

### Problem 13

**570. Managers with at Least 5 Direct Reports**

```sql
-- Solution
SELECT e1.name FROM Employee e1
LEFT JOIN Employee e2
ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;
```

### Problem 14

**1934. Confirmation Rate**

```sql
-- Solution
```

---

## Basic Aggregate Functions

### Problem 15

**620. Not Boring Movies**

```sql
-- Solution
SELECT id, movie, description, rating FROM Cinema
WHERE MOD(id, 2) = 1 and description != "boring"
ORDER BY rating DESC;
```

### Problem: 16

**1251. Average Selling Price**

```sql
-- Solution
SELECT p.product_id,
       COALESCE(
           ROUND(SUM(u.units * p.price) / NULLIF(SUM(u.units), 0), 2),
           0
       ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u
  ON p.product_id = u.product_id
 AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id
ORDER BY p.product_id;
```
