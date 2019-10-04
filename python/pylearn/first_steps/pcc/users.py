
class User:
    """Try it yourself 9-3"""

    def __init__(self, name, surname, age, sex, education):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.education = education
        self.login_attempts = 0

    def describe_user(self):
        print("Name:\t" + self.name.title() + "\nSurname:\t" +
              self.surname.title() + "\nAge:\t" + str(self.age) +
              "\nSex:\t" + self.sex + "\nEducation:\t" +
              self.education + "\nLogin:\t" + str(self.login_attempts) +
              "\n")

    def greet_user(self):
        print("Hello, " + self.name.title() + " " +
              self.surname.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """Try iy yourself 9-8"""
    def __init__(self):
        """Initialize the battery's attributes."""
        self.privileges = ('can add post', 'can delete post',
                           'can ban user', 'can fuck your mama')

    def show_privileges(self):
        print("Admin can: " + ', '.join(i for i in self.privileges) + ".")


class Admin(User):
    """Try iy yourself 9-7"""
    def __init__(self, name, surname, age, sex, education):
        super().__init__(name, surname, age, sex, education)
        self.priviliges = Privileges()

    def describe_user(self):
        print("Name:\t" + self.name.title() + "\nSurname:\t" +
              self.surname.title() + "\nAge:\t" + str(self.age) +
              "\nSex:\t" + self.sex + "\nEducation:\t" +
              self.education + "\nLogin:\t" + str(self.login_attempts) +
              "\n" + "And this is fucking ADMIN!!!" + "\n")
