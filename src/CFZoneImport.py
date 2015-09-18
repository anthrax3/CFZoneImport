import sys
import traceback
import os
import json
from colorama import init,Fore,Back,Style


from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController,expose
from cement.core import handler

# from cement.core import foundation,handler

sys.path.append(os.getcwd())

import baseController
import Config

class CFZoneImport():
    # class Meta:
    #     label = 'CFZoneImport'
    #     base_controller = 'base'
    #     handlers = [baseController, Config]
    
    # def init(self):
        # pass

    def run(self):
        try:
            app = CementApp('CFZoneImport')
            handler.register(baseController.baseController)
            handler.register(Config.Config)

            app.setup()
            app.run()
        except Exception as e:
            print "\n%s%s%s[!] Error: %s\n\n%s%s%s\n" % (Style.BRIGHT, Back.RED,Fore.WHITE, str(e),Style.NORMAL, traceback.format_exc(), Style.RESET_ALL)
            # print traceback.format_exc()
        finally:
            app.close()

c = CFZoneImport()
c.run()
