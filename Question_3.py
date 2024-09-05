# Create a class DatabaseConnection that ensures only one instance of the class can exist (Singleton pattern). 
# Implement methods to connect, disconnect, and show the connection status. 
# Then, create a metaclass that enforces a naming convention on any class inheriting from it to start with DB.


"""
# I have created a metaclass that enforces a naming convention on any class inheriting from it to start with DB. I just understand this much and created a class accordingly.
        
class DBMeta(type):
    def __new__(cls, name, bases, attrs):
        if not name.startwith('DB'):
            raise NameError("Class name must start with 'DB'")
        return super().__new__(cls, name , bases, attrs)
    
"""

class DatabaseConnection:
    __instanse = None

    def __init__(self):
        if DatabaseConnection.__instanse is not None:
            raise Exception("This is Singleton! ")
        else:
            DatabaseConnection.__instanse = self
            self.connection = None

    def connect(self, host ,user_id, password, database):
        self.__password = password
        self.connection = print(f"{user_id} Connected to {database} on {host}")
        return self.connection
    
    def disconnect(self):
        self.connection = None
        return print("Dissconnected from Database.")

    def connection_status(self):
        if self.connection:
            return print(f"Connected to {self.connection}")
        else:
            return print("No Active Connection!")



db = DatabaseConnection()
db.connection_status()
db2= DatabaseConnection()          #Uncomment to see the Exception error.
db.connect("localhost", "user", "password", "mydatabase")
db.disconnect()
db.connection_status()