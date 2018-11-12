```
In the accounts table, there is a column holding the website for each company.
The last three digits specify what type of web address they are using.
A list of extensions (and pricing) is provided here.
Pull these extensions and provide how many of each website type exist in the
accounts table.
```

SELECT RIGHT(website, 3) AS extension, COUNT(*) AS num
  FROM accounts
GROUP BY 1
ORDER BY 2 DESC;

```
There is much debate about how much the name (or even the first letter of a
company name) matters. Use the accounts table to pull the first letter of
each company name to see the distribution of company names that begin with
each letter (or number).
```
SELECT LEFT(name, 1) AS first_letter, COUNT(*)
  FROM accounts
GROUP BY 1
ORDER BY 2 DESC;

```
Use the accounts table and a CASE statement to create two groups: one group
of company names that start with a number and a second group of those company
names that start with a letter. What proportion of company names start with
a letter?
```

SELECT SUM(num) AS nums, SUM(letter) AS letters
  FROM (SELECT CASE WHEN LEFT (name,1) IN ('0','1','2','3','4','5','6','7','8','9') THEN 1 ELSE 0 END AS num,
               CASE WHEN LEFT (name,1) IN ('0','1','2','3','4','5','6','7','8','9') THEN 0 ELSE 1 END AS letter
          FROM accounts) t1;

```
Consider vowels as a, e, i, o, and u.
What proportion of company names start with a vowel,
and what percent start with anything else?
```
SELECT SUM(vowels) AS vowels_num, SUM(others) AS others_num
  FROM (SELECT CASE WHEN LEFT (UPPER(name),1) IN ('A','O','E','I','U') THEN 1 ELSE 0 END AS vowels,
               CASE WHEN LEFT (UPPER(name),1) IN ('A','O','E','I','U') THEN 0 ELSE 1 END AS others
          FROM accounts) t1;

```
Use the accounts table to create first and last name columns
that hold the first and last names for the primary_poc.
```
SELECT LEFT(primary_poc, POSITION(' ' IN primary_poc)-1) AS first_name,
       RIGHT(primary_poc, LENGTH(primary_poc)-POSITION(' ' IN primary_poc)) AS last_name
  FROM accounts;

```
Now see if you can do the same thing for every rep name in the sales_reps table.
Again provide first and last name columns.
```
SELECT LEFT(name, POSITION(' ' IN name)-1) AS first_name,
       RIGHT(name, LENGTH(name)-POSITION(' ' IN name)) AS last_name
  FROM sales_reps;

```
Each company in the accounts table wants to create an email address for each
primary_poc. The email address should be the first name of the primary_poc .
last name primary_poc @ company name .com.
```
SELECT LOWER(first_name)||'.'||LOWER(last_name)||'@'||REPLACE(name, ' ', '')||'.com' AS email
  FROM (SELECT LEFT(primary_poc, POSITION(' ' IN primary_poc)-1) AS first_name,
       RIGHT(primary_poc, LENGTH(primary_poc)-POSITION(' ' IN primary_poc)) AS last_name,
       name
          FROM accounts) t1;

```
We would also like to create an initial password, which they will change after
their first log in. The first password will be the first letter of the
primary_poc's first name (lowercase), then the last letter of their first
name (lowercase), the first letter of their last name (lowercase), the last
letter of their last name (lowercase), the number of letters in their first
name, the number of letters in their last name, and then the name of the
company they are working with, all capitalized with no spaces.
```
SELECT LOWER(first_name)||'.'||LOWER(last_name)||'@'||REPLACE(name, ' ', '')||'.com' AS email,
LEFT(LOWER(first_name),1)||RIGHT(LOWER(first_name),1)||LEFT(LOWER(last_name),1)||RIGHT(LOWER(last_name),1)||LENGTH(first_name)||LENGTH(last_name)||UPPER(REPLACE(name, ' ', '')) AS password
  FROM (SELECT LEFT(primary_poc, POSITION(' ' IN primary_poc)-1) AS first_name,
       RIGHT(primary_poc, LENGTH(primary_poc)-POSITION(' ' IN primary_poc)) AS last_name,
       name
          FROM accounts) t1;
