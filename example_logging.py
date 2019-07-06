import logging

# Exists 5 levels of logging (asc order): DEBUG, INFO, WARNING, ERROR и CRITICAL.

# add filemode="w" to overwrite
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    filename="sample.log", level=logging.ERROR, filemode='w')

logging.debug(u'This is a debug message')

logging.info(u'This is an info message')

logging.warning(u'This is a warning')

logging.error(u'This is an error message')

logging.critical(u'FATAL!!!')
