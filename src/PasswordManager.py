import re


class BasePasswordManager:
    def __init__(self):
        self.old_passwords = ["TekSystems@123"]

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, inputString):
        return bool(self.old_passwords[-1] == inputString)


class PasswordManager(BasePasswordManager):

    def get_level(self, inputPassword):
        regLevel2 = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        regLevel1 = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,20}$"
        regLevel0 = "^(?=.*[a-z])(?=.*\d)[a-z\d]{6,20}$"
        pat2 = re.compile(regLevel2)
        mat2 = re.search(regLevel2, inputPassword)
        pat1 = re.compile(regLevel1)
        mat1 = re.search(pat1, inputPassword)
        pat0 = re.compile(regLevel0)
        mat0 = re.search(pat0, inputPassword)
        if mat2:
            return 2
        elif mat1:
            return 1
        elif mat0:
            return int(0)
        else:
            return int(0)

    def set_password(self, newPassword):
        oldPasswordLevel = self.get_level(self.old_passwords[-1])
        newPasswordLevel = self.get_level(newPassword)

        if newPasswordLevel < oldPasswordLevel:
            print("""Error: New password must meet the following criteria:-
                      1. Should have at least one number.
                      2. Should have at least one uppercase and one lowercase character.
                      3. Should have at least one special symbol.
                      4. Should be between 6 to 20 characters long.
                  """)

        else:
            self.old_passwords.append(newPassword)
            return "Password Updated Successfully!"


def main():
    pm = BasePasswordManager()
    pm = PasswordManager()

    print(""" Welcome to Simplilearn Password Manager
          
          What would you like to do today ?
          
          (1) Show Current Password
          (2) Validate current Password
          (3) Set a new password
          (4) Check security level of a password
          (q) Quit
          """)

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your Current Password is:")
            print(pm.get_password())
        elif choice == "2":
            password = input(
                "Enter a password to match with your current password: ")
            print(pm.is_correct(password))
        elif choice == "3":
            newPassword = input(str("Enter a new password: "))
            print(pm.set_password(newPassword))
        elif choice == "4":
            passwordCheck = input("Enter a password to check it's security Level: ")
            print("Security level of entered password is: ", end=" ")
            print(pm.get_level(passwordCheck))
        elif choice == "q":
            done = True
            print("Thank you for using Simplilearn Password Manager")
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
