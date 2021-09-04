


class database:
    users = []
    count = 0

    @classmethod
    def find_user(cls,user_id):
        for user in cls.users:
            if user['Id'] == user_id:
                print(user)
            return user
        return 'not found'

def security(check):
    def inner(*args, **kwargs):
        password = 1234
        checkPassword = int(input("Enter the PIN Number: "))
        if password == checkPassword:
            check(*args, **kwargs)
        else:
            print("Check Your PIN Number try Again!")
            inner(*args, **kwargs)
    return inner


