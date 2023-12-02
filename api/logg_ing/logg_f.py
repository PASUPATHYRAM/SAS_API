import logging
import os
from logging.handlers import RotatingFileHandler

# log=logg_ing.getLogger(__name__)
#
# if not os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__name__),"log.log"))):
#     file = open('"os.path.abspath(os.path.join(os.path.dirname(__name__),"log.log")"','w')
#
# a=logg_ing.basicConfig(filename='log.log',filemode='a',level=logg_ing.ERROR,format="%(created)s - %(asctime)s - %(mesaage)s")
# log.addHandler(a)

class Loggercheck:
    def __init__(self):
        self.log=logging.getLogger(__name__)
        self.log.setLevel(logging.ERROR)
        self.formatter=logging.Formatter("%(asctime)s - %(created)s - %(message)s")

        if not os.path.exists(os.path.abspath(os.path.join(os.path.dirname(__name__),"log.log"))):
            file = open(os.path.abspath(os.path.join(os.path.dirname(__name__),"log.log")),'w')
            file.close()
        self.file_handler=logging.FileHandler("log.log")
        self.file_handler.setFormatter(self.formatter)
        self.log.addHandler(self.file_handler)

    def logg_check(self,message):
        self.log.error(message)




