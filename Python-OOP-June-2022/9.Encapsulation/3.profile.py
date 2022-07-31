class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if_lenght_valid = len(value) >= 8
        is_upper_case_presented = [char for char in value if char.upper()]
        is_digit_presented = [char for char in value if char.isdigit()]

        if not if_lenght_valid or not is_upper_case_presented or not is_digit_presented:
            raise ValueError("The password must contain ")
