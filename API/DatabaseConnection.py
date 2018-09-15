class DatabaseConnection:
    def __init__(self, databaseName: str, hostUrl: str):
        self.__databaseName = databaseName
        self.__hostUrl = hostUrl
        self.__connectToMongoDB()

    def __connectToMongoDB(self):
        from mongoengine import connect
        try:
            connect(self.__databaseName, host=self.__hostUrl)
        except(Exception):
            import sys
            sys.exit("Cannot connect to the database.")
