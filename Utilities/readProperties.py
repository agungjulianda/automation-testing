import configparser

cofig = configparser.RawConfigParser()
cofig.read(".\\Configuration\\config.ini")

class readConfig:

    @staticmethod
    def getAppURL():
        url = cofig.get('common info','baseURL')

        return url


    @staticmethod
    def getUsername():
        username = cofig.get('common info','username')

        return username
    
    @staticmethod
    def getPassword():
        password = cofig.get('common info','password')

        return password

    @staticmethod
    def getdefOTP():
        otp = cofig.get('common info','defOTP')

        return otp

    @staticmethod
    def getcardNumber():
        carnumber = cofig.get('common info','cardNumber')

        return carnumber