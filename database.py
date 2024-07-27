import pymysql
from tkinter import messagebox


def connect_database():
    global mycursor, conn  #global allows us to use operators like mycursor, conn in different variables
    try:
        conn=pymysql.connect(host='localhost',user="root",passwd="Shekhar@6352")
        mycursor=conn.cursor()
    except:
        messagebox.showerror("Error", "Something went wrong, Please open MySQL app before running again")
        return


    mycursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")
    mycursor.execute("USE employee_data")
    mycursor.execute("CREATE TABLE IF NOT EXISTS data(Id VARCHAR(20), Name VARCHAR(20), Phone VARCHAR(20), Role VARCHAR(20), Gender VARCHAR(20), Salary DECIMAL(10,2))")


def insert(id, name, phone, role, gender, salary):
    mycursor.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)", (id, name, phone, role, gender, salary))
    conn.commit()

def id_exists(id):
    mycursor.execute("SELECT COUNT(*) FROM data WHERE Id = %s",id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute("SELECT * FROM data")
    result=mycursor.fetchall()
    return result


def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    mycursor.execute("UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s", (new_name, new_phone, new_role, new_gender, new_salary, id))
    conn.commit()

def delete(id):
    mycursor.execute("DELETE FROM data WHERE Id = %s",id)


def search(option,value):
    mycursor.execute(f"SELECT * FROM data WHERE {option}=%s",value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute("TRUNCATE TABLE data")
    conn.commit()


connect_database()