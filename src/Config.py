from cement.core import handler
from colorama import init, Fore, Style
import configparser2
import os

class Config(handler.CementBaseHandler):
    class Meta:
        # interface = Config
        label = 'Config'
        stacked_on = 'base'

    configFile = None
    # configFile = self.app.rootPath + "/CFZoneImport.conf"
    # @controller.expose(hide=True)
    def process(self):
        print "CONFIG"
        # path of config file. Example: /usr/local/share/CFZoneImport/CFZoneImport.conf
        # self.configFile = os.path.dirname(os.path.abspath(__file__)) + "/CFZoneImport.conf"

        configFile = self.app.rootPath + "/CFZoneImport.conf"
        print self

        if not self.__checkConfig():
            raise Exception("Config file (%s) does not exist!" % self.configFile)

        self.parser = ConfigParser()

        self.__parseConfig()
        return self.parser


    def __checkConfig(self):
        if self.app.verbose:
            print "Checking if config file (%s) exists..." % self.configFile

        if os.path.isfile(self.configFile):
            return True
        else:
            return False

    def __parseConfig(self):
        if not self.parser.read(self.configFile):
            raise Exception("Unable to read config: " + self.configFile)

        return True
