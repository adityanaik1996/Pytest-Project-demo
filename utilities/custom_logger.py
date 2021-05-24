import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..."))
import inspect
import logging

def customLogger(logLevel=logging.ERROR):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]     #This will take filename passed as loggerName
    logger = logging.getLogger(loggerName)
    #logger = logging.getLogger()
    # By default, log all messages
    logger.setLevel(logging.ERROR)

    fileHandler = logging.FileHandler("automation.log")
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
