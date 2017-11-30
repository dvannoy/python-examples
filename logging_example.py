import logging.config
from config.config import LOG_CONFIG_PATH, LOG_LEVEL

logging.config.fileConfig('config/logging.conf')
log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)

example_list = ['item1', 'item2', 'item3', 4, 10]
#print("Loop through example list")
log.debug("Loop through example list")
if __name__ == "__main__":
    for i in example_list:
        try:
            #print("Value = %s" % i)
            log.info("Value = %s", i)
        except TypeError as e:
            #print("Error in list item %s" % i)
            log.error("Error in list item", i)
            log.exception("Exception")


