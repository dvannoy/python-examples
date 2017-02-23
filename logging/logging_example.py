import logging.config

from config.config import LOG_CONFIG_PATH, LOG_LEVEL

logging.config.fileConfig(LOG_CONFIG_PATH)
log = logging.getLogger('logging_example')
log.setLevel(LOG_LEVEL)

example_list = ['item1', 'item2', 'item3', 4, 10]

log.debug("Loop through example list")
for i in example_list:
    try:
        print(i)
    except TypeError as e:
        log.error("Error in list item", i)
        log.exception("Exception")



