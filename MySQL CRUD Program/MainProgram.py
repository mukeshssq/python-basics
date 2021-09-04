from userslist import database
from userslist import security
from mysql_connection import DBConnector
class Employee(database):

    @classmethod
    def create(cls):
        name = input("Enter your name: ")
        DBConn = DBConnector()
        response = DBConn.insertUser(name)
        # print(cls.users)

    @classmethod
    def get_users(cls):
        user_id = int(input("select your Id: "))
        # check = cls.find_user(user_id)
        # print(check)
        DBCConn = DBConnector()
        response = DBCConn.getUserName(user_id)

    @classmethod
    def update_user(cls):
        user_id = int(input("select update the user Id: "))
        new_name = input("update the New name: ")
        DBConn = DBConnector()
        response = DBConn.updateUserData(user_id, new_name)

    @classmethod
    @security
    def delete_user(cls):
        userId = int(input("select user id to delete: "))
        DBConn = DBConnector()
        response = DBConn.deleteUser(userId)

    @classmethod
    def getAllUsers(cls):
        DBConn = DBConnector()
        response = DBConn.getAllUsers();

    @classmethod
    def exitloop(cls):
        print("Exit successfully")

    @classmethod
    def main(cls):
        while True:
            select_option = {
                1 : 'Add user',
                2 : 'Get user',
                3 : 'Update user',
                4 : 'delete user',
                5 : 'Get All Users',
                6 : 'Exit program'
            }
            print(select_option)
            option = int(input('select items on the list: '))
            if option == 1:
                cls.create()
            elif option == 2:
                cls.get_users()
            elif option == 3:
                cls.update_user()
            elif option == 4:
                cls.delete_user()
            elif option == 5:
                cls.getAllUsers()
            elif option >6:
                print('Invalid Number')
            elif option == 6:
                cls.exitloop()
                break
Employee.main()




