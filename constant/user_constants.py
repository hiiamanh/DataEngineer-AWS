import configparser


class UserConstants:
    def __init__(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)

        self.KEY = config.get('AWS', 'KEY')
        self.SECRET = config.get('AWS', 'SECRET')
        self.REGION = config.get('AWS', 'REGION')
