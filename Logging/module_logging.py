# https://middleware.io/blog/python-logging-best-practices/
import logging

root_logger = logging.getLogger()
logging.basicConfig()

module_logger = logging.getLogger('module_logger')
module_logger.propagate = False

child_logger = logging.getLogger('module_logger.child_logger')
child_logger.setLevel('DEBUG')
child_logger.propagate = True

custom_handler = logging.StreamHandler()
module_logger.addHandler(custom_handler)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s")
custom_handler.setFormatter(formatter)

file_handler = logging.FileHandler("test.log", mode="a")
file_handler.setFormatter(formatter)
module_logger.addHandler(file_handler)

def main():
    # print(root_logger, root_logger.handlers, sep=" | ")
    # print(module_logger, module_logger.handlers, sep=" | ")
    # print(module_logger.parent)
    # print(child_logger, child_logger.handlers, sep=" | ")
    # print(child_logger.parent)

    child_logger.debug("Hello guy!")


if __name__ == "__main__":
    main()
