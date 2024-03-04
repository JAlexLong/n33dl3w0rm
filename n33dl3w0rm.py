from lxml import etree
from time import time
import os
import logging
import socket
import sys



def main():
    start_time = time()
    logger = create_logger("n33dl3w0rm")

    tcp_test_response = test_tcp_connection()


    logger.info(tcp_test_response.decode())
    logger.info(f"n33dl3w0rm took {round(time() - start_time, 6)} seconds to run.")


def test_tcp_connection():
    target_host = "www.google.com"
    target_port = 80

    # create a socket object
    # * AF_INET --> IPv4 Address or Hostname
    # * SOCK_STREAM --> TCP connection

    # ! Make sure this is actually works as a context manager
    # * It seems to work, but more testing is needed to verify
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        # connect the client
        client.connect((target_host, target_port))

        # send some data
        client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

        # receive some data
        response = client.recv(4096)
    return response


def create_logger(name):
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )

    file_handler = logging.FileHandler('log/log.txt', mode='w')
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)

    logger_ = logging.getLogger(name)
    logger_.setLevel(logging.DEBUG)
    logger_.addHandler(file_handler)
    logger_.addHandler(stream_handler)

    return logger_


if __name__ == "__main__":
    main()
