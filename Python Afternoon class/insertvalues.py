import sqlite3

conn= sqlite3.connect("company.db")
print("Connected")

conn.execute("INSERT INTO company1(ID, FIRSTNAME, LASTNAME,AGE,SALARY,TASK)\
             VALUES (1,'Andrew', 'Mark', 21, 30000.00,'Manager')");
conn.execute("INSERT INTO company1(ID, FIRSTNAME, LASTNAME,AGE,SALARY,TASK) \
             VALUES (2,'Tom', 'KSI', 23, 900000.00,'Manager')");
conn.execute("INSERT INTO company1(ID, FIRSTNAME, LASTNAME,AGE,SALARY,TASK)\
             VALUES (3,'Vic', 'Tobi', 22, 920890.00,'Trainer')");

conn.commit()
print("Successfully inserted values in company1")