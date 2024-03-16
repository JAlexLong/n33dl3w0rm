from lxml import etree
from time import time
import logging
import os
import socket
import sys


def main():
    start_time = time()
    logger = create_logger("n33dl3w0rm")

    target_host = "www.github.com"
    logger.debug(f"Testing connection at {target_host}")

    # test tcp client
    try:
        tcp_test_response = test_tcp_connection(target_host)
        logger.info(tcp_test_response.decode())
    except KeyboardInterrupt as e:
        logger.warning(e)

    # test udp client
    try:
        udp_test_data = test_udp_connection()
        logger.info(udp_test_data.decode())
    except KeyboardInterrupt as e:
        logger.warning("Exception raised: KeyboardInterrupt, during test_udp_connection()")

    logger.info(f"n33dl3w0rm took {round(time() - start_time, 6)} seconds to run.")
    return True


def test_tcp_connection(target_host="www.github.com", target_port=80):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host, target_port))

    # send some data
    client.send(b"GET / HTTP/1.1\r\nHost: www.github.com\r\n\r\n")

    # receive some data
    response = client.recv(4096)
    return response


def test_udp_connection(target_host="127.0.0.1", target_port=9997):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # send some data
    client.sendto(b"AAABBBCCC", (target_host, target_port))

    # receive some data
    data, addr = client.recvfrom(4096)
    print(data.decode())
    client.close()
    return data


def create_logger(name):
    # add timestamps to log entries
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )

    # write log entries in the specified log file
    # ! log will be overwritten each time this is ran
    file_handler = logging.FileHandler('log/log.txt', mode='w')
    file_handler.setFormatter(formatter)

    # also direct log output to stdout aka the console
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)

    # create logger
    # * Note that the _ in logger_ is from the book and is assumed to be
    # * because of the convention that uses terminating _ to differentiate
    # * between variables and keywords/modules (aka sys_ vs sys)
    logger_ = logging.getLogger(name)
    logger_.setLevel(logging.DEBUG)
    logger_.addHandler(file_handler)
    logger_.addHandler(stream_handler)

    return logger_


if __name__ == "__main__":
    main()
