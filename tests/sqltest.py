import sqlite3



db=sqlite3.connect("new.db")
cursor0=db.cursor()
insert_query= """INSERT INTO `users`
                          ('name', 'password', 'address')
                           VALUES
                          ('amir0',1234,42146)"""

#cursor0.execute(insert_query)
db.commit()

#cursor0.close()
def insertVaribleIntoTable( name, password, address):

        #sqliteConnection = sqlite3.connect('SQLite_Python.db')
        #cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO `users`
                          ('name', 'password', 'address') 
                           VALUES 
                          (?,?,?)"""
        data_tuple = ( name, password, address)
        cursor0.execute(sqlite_insert_with_param, data_tuple)
        db.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")



        cursor0.close()

def selectuserfrom_table(name,password):
    # sqlite_select_query = """SELECT * from users
    #  where name = ?
    #  AND password = ?"""
    #usr=(name,password)
    cursor0.execute( """SELECT name,password from users
     where name = ?
     AND password = ?""",(name,password))
    records=cursor0.fetchall()

    print(dir(cursor0))
    for row in records:
        print("Name = ", row[0])
        print("Pssword  = ", row[1])
       # print("address  = ", row[2])
        if (password==row[1]):
            print("password is good")
    cursor0.close()

selectuserfrom_table("yosef1",66666)


#insertVaribleIntoTable("yosef1",66666,1221435)