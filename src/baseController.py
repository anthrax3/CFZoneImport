from cement.core import handler,controller,backend
from cement.utils.misc import init_defaults
from colorama import init, Fore, Back, Style
from pprint import pprint
import os

import Config
# import CrimeFlare

class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Imports crimeflares.com IPs and creates bind9 zones'

        config_defaults = dict(
                    debug = False,
                    config = os.path.abspath(__file__ + "../") + "/CFZoneImport.conf",
                )

        arguments = [
                (['-v', '--verbose'], dict(action='store_true', help='Verbose Output')),
                (['-c', '--config'], dict(action='store', help='specify alternate config file'))
                ]
        epilog = "Sample Usage: cfzi [-c /path/to/config.conf] [--update] [-v]"

    @controller.expose(hide=True, aliases=['run'])
    def default(self):

        self.app.rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config = Config
        # self.Config = Config.Config()
        # self.Config.process()
        print self


        # crimeFlare = CrimeFlare()
        # crimeFlare.process()
        
        print "CFZI"
