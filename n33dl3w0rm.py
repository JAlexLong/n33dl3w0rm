from lxml import etree
from time import time
import os
import logging
import socket



def main(log_lvl=logging.INFO):
    start_time = time()

    target_host = "www.google.com"
    target_port = 80

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    # send some data
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # receive some data
    response = client.recv(4096)

    logging.info(response.decode())
    # TODO I wonder if this means I can open client in a context manager
    client.close()

    #log_host_data(log_lvl)
    print(f"n33dl3w0rm took {round(time() - start_time, 6)} seconds to run.")


def log_host_data(log_lvl):
    logging.basicConfig(filename='log/data.log',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        encoding='utf-8',
                        level=log_lvl,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    logging.info(f"os.getpid() --> {os.getpid()}")
    logging.info(f"os.getcwd() --> {os.getcwd()}")
    logging.info(f"os.getlogin() --> {os.getlogin()}")

if __name__ == "__main__":
    main(log_lvl=logging.DEBUG)
