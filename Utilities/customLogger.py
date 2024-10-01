import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = "./Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format='%(asctime)s: %(levelname)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )
        logger = logging.getLogger()
        return logger

