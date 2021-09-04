import mysql.connector
from mysql.connector import Error


class DBConnector:
    def insertUser(self, name):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='library',
                                                 user='root',
                                                 password='')

            print('Planning to insert :' + name)
            mysql_insert_table = "INSERT INTO users (name) VALUES ('{}');".format(name)
            print('query: ' + mysql_insert_table)
            cursor = connection.cursor()
            cursor.execute(mysql_insert_table)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into table!!")
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def create_table(self):
        connection = mysql.connector.connect(host='localhost',
                                             database='users',
                                             user='root',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

        mysql_create_tablename = '''CREATE TABLE users(
                    Id int(11) NOT NULL,
                    Name varchar(25),
                    PRIMARY KEY(Id))'''
        cursor = connection.cursor()
        reslut = cursor.execute(mysql_create_tablename)
        print('useres table has created')

    def updateUserData(self, userId, updatedUserName):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='library',
                                                 user='root',
                                                 password='')

            print('Planning to update :' + updatedUserName)
            print(userId)

            userUpdateQuery = "update users set name ='{}' where id = {};".format(updatedUserName, userId)
            print('query: ' + userUpdateQuery)

            cursor = connection.cursor()

            cursor.execute(userUpdateQuery)
            connection.commit()

            print(cursor.rowcount, "Record updated successfully into table!!")
            cursor.close()
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def getUserName(self, userId):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='library',
                                                 user='root',
                                                 password='')
            print('planned for get particular userId: ', userId)
            getUserQuery = 'select * from users where id = {}'.format(userId)
            print("Query", getUserQuery)
            cursor = connection.cursor()

            cursor.execute(getUserQuery)
            # connection.commit()
            records = cursor.fetchall()
            print('Data :', records)
            # print(cursor.rowcount, "get data successfully into table!!")
            cursor.close()


        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def deleteUser(self, userId):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='library',
                                                 user='root',
                                                 password='')
            print('planned for delete particular userId: ', userId)
            DeleteUserQuery = 'delete from users where id = {}; '.format(userId)
            print("Query", DeleteUserQuery)
            cursor = connection.cursor()

            cursor.execute(DeleteUserQuery)
            connection.commit()
            print(cursor.rowcount, "data delete successfully into table!!")
            cursor.close()


        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


class DBConnector:
    def getAllUsers(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='library',
                                                 user='root',
                                                 password='')

            print('Trying to all users...')
            getAllUsers = 'select * from users;';
            print('query: ' + getAllUsers)
            cursor = connection.cursor()
            cursor.execute(getAllUsers)
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)
            print("\nPrinting each row :")
            for row in records:
                print("Id :", row[0], ", Name:", row[1])
                print("---------------------------")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
