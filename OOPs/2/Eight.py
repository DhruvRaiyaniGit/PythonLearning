
class Password:
    def __init__(self, password):
        self.__password = password

    def set_password(self, password):
        if len(password) >= 10:
            self.__password = password
        else:
            print('weak password')

    def get_password(self):
        return self.__password

    def print_password_len(self):
        print("Your password length is ", len(self.__password))


pwOne = Password("RadheShaym")
pwOne.print_password_len()
pwOne.set_password('aafasdfdsasfaa')
pwOne.print_password_len()
pwd = pwOne.get_password()
print('updated password is',pwd)

