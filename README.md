# assignment_2.6-roni
the client connects to a server (running on IP 127.0.0.1 and port 1729),
sends commands in input entered by the user
and displays the servers responses.
the connection continues in a loop until user types EXIT.
the server listens for client connections on port 1729,
receives commands (every one up to 4 bytes), acts on
the requested action and sends back a response.
for each of these commands this action is printed on th clients side:
TIME - returns the current date and time
NAME - returns the server name
RAND - returns a random integer number (1–10)
EXIT - ends the client connection
