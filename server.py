"""
author: Roni Prital

date: october 2025

server side of a client-server system.
the server listens for client connections on port 1729,
receives commands (every one up to 4 bytes), acts on
the requested action and sends back a response.

for each of these commands this action is printed on th clients side:
TIME - returns the current date and time
NAME - returns the server name
RAND - returns a random integer number (1–10)
EXIT - ends the client connection
"""
from datetime import datetime
import random
import socket
import logging

QUEUE_LEN = 1
MAX_PACKET = 4
ACTIVE_SERVER = True

"""
lays out the logging system
"""
def main():
        print()
if __name__ == '__main__':
    log_format = '%(levelname)s: %(message)s'
    log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format=log_format)
main()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:

    my_socket.bind(('0.0.0.0', 1729))

    my_socket.listen(QUEUE_LEN)

    logging.info("server on, listening on port 1729")


     #waits for the client to connect and when client connects
     #returns a client_socket() to communicate with that client
    while ACTIVE_SERVER:
        client_socket, client_address = my_socket.accept()

        try :

            while True:
                request = client_socket.recv(MAX_PACKET).decode()

                # checks that input is not empty if it is AserrtionError and program stopped
                assert request.strip() != "", "empty request received"


                if request == "EXIT":
                    # ends the client connection when command = EXIT
                    logging.info("response is EXIT\n server exited")
                    break

                elif request == "TIME":
                    # sends the current date and time
                    now = datetime.now()
                    response = str(now)
                    logging.info("response is TIME")


                elif  request == "NAME":
                    # sends the servers name
                    strg = "Roni's server"
                    response = strg
                    logging.info("response is NAME")

                elif request == "RAND":
                    # returns a random integer number from 1-10
                    response = str(random.randint(1, 10))
                    logging.info("response is RAND")

                else:
                    # prints warning for unknown commands
                    response = "unknown command"
                    logging.debug(f"request is:{request}")
                    logging.warning(f"unknown command: {request}")

                # sends the response back to the client
                client_socket.send(response.encode())


        except socket.error as err:

            print('received socket error on client socket' + str(err))

        finally:
            # closes client connection
            client_socket.close()
            logging.info("closed connection with client")

except socket.error as err:

    print('received socket error on server socket' + str(err))

finally:
    my_socket.close()


