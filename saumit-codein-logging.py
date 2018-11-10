"""this is a program to show the two levels of logging:
		1-INFO level(colored) in STDOUT
		2-DEBUG level,which will display log to a log file-log.txt

	for an example i am taking the sum and the product of 2 numbers where this is the basic program:

	 a = 10
              b = 15

              print(a+b)
              print(a*b)

So I am going to replace the print statement with logging statements	and along with the date and time format.

There is a log file named codeinlog.txt

By - SAUMIT PRADHAN-saumitp5@gmail.com
"""

import coloredlogs, logging
import logging.config
import sys

logging.basicConfig( filename =' codeinlog.txt', level=logging.DEBUG,format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')  #For the Date-Time and levelname 

coloredlogs.install(level='INFO')

coloredlogs.DEFAULT_LEVEL_STYLES = {'info': {'color': 'red', 'bold': True}}         #For changing the INFO color
logger = logging.getLogger(__name__)

handler = logging.StreamHandler(sys.stdout)              #This was done to create a STDOUT as per the task
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

a = 10  #The 2 integers 10 and 15
b = 15


logger.info(a+b)         #INFO level logging
logger.info(a*b)

logger.debug(a+b)      # DEBUG level logging
logger.debug(a*b)



