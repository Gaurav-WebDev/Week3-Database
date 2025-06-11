import mysql.connector


# ===> Database Config
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root", # your password
    database = "testDemo"
)

print("Database Connected!")

cursor = conn.cursor()

# ===> C : Create ( Insert Data into Database without user input )

sql = "INSERT INTO students(name , age , course) VALUES(%s , %s , %s)"
values = [("Raj" , 24 , "MBA") , ("Mohan" , 34 , "MCA") , ("Vikash" , 26 ,"BSc") , ("Raman" , 26 , "MCA")]

cursor.executemany(sql , values)
conn.commit()

# ===> C : Create ( Insert Data into Database with user input )

# sql = "INSERT INTO students(name , age , course) VALUES(%s , %s , %s)"
# name = input("Enter Student Name : ")
# age = int(input("Enter your age : "))
# course =  input("Enter Course Name :")
# values = (name , age , course)

# cursor.execute(sql , values)
# conn.commit()

print(cursor.rowcount , "record inseted!")

conn.close()