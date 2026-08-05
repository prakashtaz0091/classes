# Assignment - File Handling

## Question 1: Student Marks Management

You are given a CSV file named `marks.csv` with the following data:

```csv
Roll,Name,Math,Science,English
1,Ram,80,75,90
2,Sita,65,70,60
3,Hari,90,88,95
4,Gita,50,55,45
```

Write a Python program that:

1. Reads the CSV file.
2. Adds three new columns:

   * `Total`
   * `Average`
   * `Result`
3. Calculate:

   * `Total = Math + Science + English`
   * `Average = Total / 3`
   * If Average >= 40, Result = `"Pass"`, otherwise `"Fail"`.
4. Save the updated data back to the same CSV file.
5. If the `Total` column already exists, display:

   ```
   Result already calculated.
   ```

   and terminate the program.

---

## Question 2: Library Book Borrowing System

You are given a CSV file named `library.csv`.

```csv
Book ID,Book Name,Student Name
101,Python Basics,Ram
102,C Programming,
103,Data Structures,Sita
104,Java,
105,DBMS,Hari
```

Write a Python program that:

1. Read the CSV file.
2. Count:

   * Total books
   * Borrowed books (Student Name is not empty)
   * Available books (Student Name is empty)
3. Add three new columns at the end:

   * `Total Books`
   * `Borrowed`
   * `Available`
4. These values should be added to every row.
5. Save the updated CSV file.
6. Prevent duplicate columns if they already exist.

---

## Question 3: Student Attendance Percentage

You are given a CSV file:

```csv
Roll,Name,2026-08-01,2026-08-02,2026-08-03,2026-08-04
1,Ram,P,P,A,P
2,Sita,A,A,P,P
3,Hari,P,P,P,P
4,Gita,A,P,A,A
```

Write a Python program that:

1. Read the CSV file.
2. Calculate for every student:

   * Total Days
   * Total Present
   * Total Absent
   * Attendance Percentage
3. Formula:

```text
Attendance Percentage = (Total Present / Total Days) × 100
```

4. Add the following columns:

   * `Total Days`
   * `Total Present`
   * `Total Absent`
   * `Attendance %`
5. Save the updated CSV file.
6. If the `Attendance %` column already exists, stop the program using `sys.exit()`.
