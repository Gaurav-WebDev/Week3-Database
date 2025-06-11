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

while True:

    print("<= Enter your choice =>")
    print("1 for Add New Student")
    print("2 for View All Students")
    print("3 for Exit")
    choice = int(input("Your Choice : "))

    if choice == 1:
        print(" --> Add New Student <--")
        sql = "INSERT INTO students(name , age , course) VALUES(%s , %s , %s)"
        name = input("Enter Student Name : ")
        age = int(input("Enter your age : "))
        course =  input("Enter Course Name : ")
        values = (name , age , course)

        cursor.execute(sql , values)
        conn.commit()

        
        print(cursor.rowcount , "record inseted!")

    elif choice == 2:
        print("--> All Students <---")
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()

        for rows in result:
            print(rows)

    elif choice == 3:
        print("Ok Bye Have a Good Day!")
        break
    else :
        print("Please choose vaild option ( 1 , 2 , 3 )")

