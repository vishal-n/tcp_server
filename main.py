import socket
import time
import logging

logging.basicConfig(level=logging.INFO)


def do(conn):
    try:
        buf = conn.recv(1024)
        if not buf:
            return

        logging.info("Processing the current request")
        time.sleep(8)

        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello, World!\r\n")

    except Exception as e:
        logging.exception(e)
    finally:
        conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 1729))
    server.listen()

    logging.info("Server listening on port 1729")

    while True:
        logging.info("Waiting for a client to connect")
        conn, addr = server.accept()
        logging.info("Client connected: %s", addr)

        do(conn)


if __name__ == "__main__":
    main()
