```
Say you're an analyst at Parch & Posey and you want to see:

*each account who has a sales rep and each sales rep that has an account
(all of the columns in these returned rows will be full)
*but also each account that does not have a sales rep and each sales rep that
does not have an account (some of the columns in these returned rows will be empty)
```

SELECT a.name, a.sales_rep_id, s.id
  FROM accounts a
FULL OUTER JOIN sales_reps s
    ON a.sales_rep_id = s.id

```
write a query that left joins the accounts table and the sales_reps tables on
each sale rep's ID number and joins it using the < comparison operator on
accounts.primary_poc and sales_reps.name, like so:

accounts.primary_poc < sales_reps.name

The query results should be a table with three columns: the account name (e.g.
Johnson Controls), the primary contact name (e.g. Cammy Sosnowski), and the
sales representative's name (e.g. Samuel Racine).
```

SELECT a.sales_rep_id, a.primary_poc, s.name
  FROM accounts a
LEFT JOIN sales_reps s
ON s.id = a.sales_rep_id AND a.primary_poc < s.name

```
One of the most common use cases for self JOINs is in cases where two events
occurred, one after another. As you may have noticed in the previous video,
using inequalities in conjunction with self JOINs is common.

* change the interval to 1 day to find web events that occur within one after
another within one day
** add a column for the channel variable in both instances of the table in your
query
```
SELECT w1.id AS w1_id,
       w1.account_id AS w1_account_id,
       w1.occurred_at AS w1_occurred_at,
       w2.id AS w2_id,
       w2.account_id AS w2_account_id,
       w2.occurred_at AS w2_occurred_at,
       w1.channel AS w1_channel,
       w2.channel AS w2_channel
  FROM web_events w1
 LEFT JOIN web_events w2
   ON w1.account_id = w2.account_id
  AND w2.occurred_at > w1.occurred_at
  AND w2.occurred_at <= w1.occurred_at + INTERVAL '1 day'
ORDER BY w1.account_id, w1.occurred_at

```
Write a query that uses UNION ALL on two instances (and selecting all columns)
of the accounts table.
```
SELECT *
  FROM accounts

UNION ALL

SELECT *
  FROM accounts

```
Add a WHERE clause to each of the tables that you unioned in the query above,
filtering the first table where name equals Walmart and filtering the second
table where name equals Disney.
```
SELECT *
  FROM accounts
WHERE name = 'Walmart'

UNION ALL

SELECT *
  FROM accounts
WHERE name = 'Disney'

```
Perform the union in your first query in a common table expression and name it
double_accounts. Then do a COUNT the number of times a name appears in the
double_accounts table. If you do this correctly, your query results should have
a count of 2 for each name.
```
WITH double_accounts AS (
SELECT *
  FROM accounts

UNION ALL

SELECT *
  FROM accounts)

SELECT name, COUNT(name) as name_count
  FROM double_accounts
GROUP BY 1
ORDER BY 2 DESC
