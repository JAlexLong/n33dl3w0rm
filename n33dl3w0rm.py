from lxml import etree
from time import time
import os
import logging

start_time = time()


def main(log_level=logging.INFO):
    logging.basicConfig(filename='log/n33dl3w0rm.log',
                        encoding='utf-8',
                        level=log_level,
                        )
    logging.info("os.getcwd()\tos.getlogin()\tos.getpid()")
    logging.info(f"{str(os.getcwd())}\t{str(os.getlogin())}\t{str(os.getpid())}")
    print("Hello, n33dl3w0rm... Welcome to your world - "
          "this rotten apple of ours...")

    print(f"n33dl3w0rm took {round(time() - start_time, 2)} seconds to run.")

if __name__ == "__main__":
    main(log_level=logging.DEBUG)