import logging
# |-- root
# |   |-- sub_1 (INFO)
# |   |-- sub_2
# |   |   |-- sub_sub_1 (DEBUG)

root_logger = logging.getLogger()
logging.basicConfig()

sub_1_logger = logging.getLogger('root_logger.sub_1_logger')
sub_1_logger.setLevel('INFO')

sub_2_logger = logging.getLogger('root_logger.sub_2_logger')
sub_2_logger.propagate = False

sub_sub_1_logger = logging.getLogger('sub_2_logger.sub_sub_1_logger')
sub_sub_1_logger.setLevel('DEBUG')


custom_handler = logging.StreamHandler()
custom_handler.setLevel('DEBUG')
formatter = logging.Formatter(fmt="%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d")
custom_handler.setFormatter(formatter)

sub_1_logger.addHandler(custom_handler)
sub_2_logger.addHandler(custom_handler)
root_logger.addHandler(custom_handler)

def main():
    # print(root_logger)
    # print(sub_1_logger)
    # print(sub_2_logger)
    # print(sub_sub_1_logger)

    sub_2_logger.debug("Hello!")
    sub_1_logger.debug("Hello!")
    sub_2_logger.debug("Hello!")
    root_logger.debug("Hello!")






if __name__ == "__main__":
    main()
