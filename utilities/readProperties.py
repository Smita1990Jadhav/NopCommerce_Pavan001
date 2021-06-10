import configparser

config=configparser.RawConfigParser()
config.read('D:\\pythonProject\\nopcommerceApp\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getEmail():
        username=config.get('common info','userEmail')
        return username
    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password