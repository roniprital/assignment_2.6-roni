"""
author: Roni Prital

date: october 2025

client side of a client-server system.
the client connects to a server (running on IP 127.0.0.1 and port 1729),
sends commands in input entered by the user
and displays the servers responses.
the connection continues in a loop until user types EXIT.
"""
import socket
import logging


def main():
    print()


if __name__ == '__main__':
    log_format = '%(levelname)s: %(message)s'
    log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format=log_format)
main()

MAX_PACKET = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:

    my_socket.connect(('127.0.0.1', 1729))
    logging.info("connected to server on 127.0.0.1 , 1729")
    while True:
    #recives input and sends it to the server, if empty AssertionError
        command = input("enter your command: ")
        assert command != "", "command cannot be empty"

        if not command:
            command = " "

        my_socket.send(command.encode())

        if command == "EXIT":
            logging.info("requested to exit")
            break

        # receives message from the server and prints it
        response = my_socket.recv(MAX_PACKET).decode()
        print(response)


except socket.error as err:
    print('received socket error ' + str(err))


#closes the socket
finally:
    my_socket.close()













