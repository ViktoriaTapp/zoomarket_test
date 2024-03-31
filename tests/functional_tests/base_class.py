import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def get_price(price: str):
        price = price.replace(" ", "")
        return int(price)

    @staticmethod
    def get_total_sum(total_sum: str):
        total_sum = total_sum.replace(" ", "")
        return int(total_sum[:-1])

    @property
    def increase_quanitity_btn_xpath(self):
        return "bx_117848907_235370_quant_up"
