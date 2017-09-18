import os
from utils.file_reader import YamlReader
#/Users/zoe/Desktop/Test_Framework-iOS/config
#BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '..／
BASE_PATH = "/Users/zoe/Desktop/Test_Framework_iOS"
CONFIG_FILE = BASE_PATH + '/config/config.yml'
DATA_PATH = BASE_PATH + '/data/'
DRIVER_PATH = BASE_PATH + '/drivers/'
LOG_PATH = BASE_PATH + '/log/'
REPORT_PATH = BASE_PATH + '/report/'


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)