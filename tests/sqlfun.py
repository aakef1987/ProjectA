import sqlite3




def addnewuser(name, password, address):
    connecttodatabase = sqlite3.connect("new.db")
    cursor = connecttodatabase.cursor()
    sqlite_insert_with_param = """INSERT INTO `users`
                      ('name', 'password', 'address') 
                       VALUES 
                      (?,?,?)"""
    cursor.execute(sqlite_insert_with_param,(name, password, address))
    connecttodatabase.commit()
    cursor.close()


def checklogin(name,password):
    connecttodatabase = sqlite3.connect("new.db")
    cursor = connecttodatabase.cursor()
    cursor.execute("""SELECT name,password from users
     where name = ?
     AND password = ?""", (name,password))
    records = cursor.fetchall()
    if (records==[]):  #check if there no result
        print("bad username or password")
        return False
    if (password==records[0][1]):
       print("password is good")
    cursor.close()

#checklogin("amir",12434)




