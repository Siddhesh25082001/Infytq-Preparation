# SQL Statements

### SELECT

- The `SELECT` statement is used to select data from a database

`Selects Particular Columns`

``` sql

SELECT column1Name, column2Name, ... FROM tableName;

```

`Selects All Columns`

``` sql

SELECT * FROM tableName;

```

`Selects Distinct Values (Rows)`

``` sql

SELECT DISTINCT column1Name, column2Name, ... FROM tableName;

```

---

### WHERE

- The `WHERE` clause is used to filter records
- It is used to extract only those records that fulfill a specified condition
- The `WHERE` clause is not only used in `SELECT` statements, but it is also used in `UPDATE`, `DELETE`, etc

``` sql

SELECT column1Name, column2Name, ... FROM tableName WHERE condition;

```

**Operations in `WHERE` Clause**

- `=`	: Equal	
- `!=`	: Not Equal
- `>`	: Greater than	
- `<`	: Less than	
- `>=`	: Greater than or Equal	
- `<=`  : Less than or Equal	
- `BETWEEN`	: Between a certain range	
- `LIKE` : Search for a pattern	
- `IN` : To specify multiple possible values for a column

--- 

### AND, OR, NOT

- The WHERE clause can be combined with AND, OR, and NOT operators
- The AND and OR operators are used to filter records based on more than one condition

`The AND operator displays a record if all the conditions separated by AND are TRUE`

``` sql

SELECT column1Name, column2Name, ... FROM tableName WHERE condition1 AND condition2 ... ;

```

`The OR operator displays a record if any of the conditions separated by OR is TRUE`

``` sql

SELECT column1Name, column2Name, ... FROM tableName WHERE condition1 OR condition2 ... ;

```

`The NOT operator displays a record if the condition(s) is NOT TRUE`

``` sql

SELECT column1Name FROM tableName WHERE NOT condition;

```

---

###  ORDER BY

- The `ORDER BY` keyword is used to sort the result-set in ascending or descending order
- By default, It is ascending order
- To sort the result-set in descending order, Use keyword `DESC`

``` sql

SELECT column1Name, column2Name, ... FROM tableName ORDER BY column1Name, column2Name ASC | DESC;

```

---

### INSERT INTO

- The `INSERT INTO` statement is used to insert new records in a table

``` sql

/* Type-1: Specifying all column names and their respective values */
INSERT INTO tableName (column1Name, column2Name, ... ) VALUES (value1, value2, ... );

/* Type-2: Specifying only column value 
Note: Here Column values must be in the same order as columnNames */
INSERT INTO tableName VALUES (value1, value2, ... );

```

---   