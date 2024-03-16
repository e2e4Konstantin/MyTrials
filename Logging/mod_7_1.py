import logging
# |-- root
# | |-- main (INFO)
# | |-- utils (DEBUG)

root_logger = logging.getLogger()

main_logger = logging.getLogger('main_logger')
main_logger.setLevel('INFO')

utils_logger = logging.getLogger('utils_logger')
utils_logger.setLevel('DEBUG')

def main():

    print(main_logger)
    print(main_logger.parent)

    print(utils_logger)
    print(utils_logger.parent)


if __name__ == "__main__":
    main()
