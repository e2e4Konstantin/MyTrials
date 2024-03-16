import logging

mod_1_logger = logging.getLogger('mod_1_logger')
mod_1_logger.setLevel('INFO')

def mod_1():
    print(mod_1_logger)
