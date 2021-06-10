import inspect
import logging

class LogGen:
    @staticmethod
    def loggen():
        loggername=inspect.stack()[1][3]#this method inbuilt give file name in logs
        logger = logging.getLogger(loggername)
        fhandler = logging.FileHandler(filename='D:\\pythonProject\\nopcommerceApp\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s : %(name)s :%(levelname)s : %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
