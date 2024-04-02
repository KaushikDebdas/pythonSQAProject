from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("D:/Study Videos/SQA/Python/pythonSQAProject/SampleProject4/configurations/config.ini")
    return config.get(category, key)