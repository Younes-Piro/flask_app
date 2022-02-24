class User:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return ("name : {0} , lastname: {1}").format(self.name , self.lastname)

    def create_user(self):
        user = {
            "name": self.name,
            "lastname": self.lastname
        }
        return user
