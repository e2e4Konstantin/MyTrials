import sys
sys.path.append('Logging')

import logging.config

from logging_config import log_conf

logging.config.dictConfig(log_conf)


# module_logger = logging.getLogger("module_logger")
# module_logger.propagate = False

# formatter = logging.Formatter(fmt="%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d")

# file_handler = logging.FileHandler("test.log", mode="a")
# file_handler.setFormatter(formatter)
# module_logger.addHandler(file_handler)

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# module_logger.addHandler(console_handler)

submodule_logger = logging.getLogger('module_logger.submodule_logger')
submodule_logger.setLevel('DEBUG')


def main():
    submodule_logger.debug("Hello!")

if __name__ == "__main__":
    main()
