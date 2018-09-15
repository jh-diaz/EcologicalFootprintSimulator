class DatabaseConnection:
    def __init__(self):
        self.connectToMongoDB()
    
    def connectToMongoDB(self):
        from mongoengine import connect
        connect("ecofootprint", host='mongodb://Joshua:12345@localhost/ecofootprint')

x = DatabaseConnection()
from Models import Country
y = Country(countryName="haha")
y.save()