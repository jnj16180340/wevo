@contextmanager
def mevo_connection(MEVO_IP="192.168.69.19", MEVO_PORT=38000):
    sock = ssl.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        keyfile=None,
        certfile=None,
        server_side=False,
        cert_reqs=ssl.CERT_NONE,
        ssl_version=ssl.PROTOCOL_TLSv1_2,
    )
    sock.connect((MEVO_IP, MEVO_PORT))
    try:
        yield sock
    finally:
        print("Cleaning up socket...", end="")
        sock.close()
        print("Done")

def maine(sequence, ):
    sendme = reduce(add, sequence)

    print("\nSENDING DATA:")
    print(sendme)

    with mevo_connection(MEVO_HOST, MEVO_PORT) as s:
        # SEND THE DATA
        s.sendall(sendme)

        # WAIT FOR A RESPONSE
        print("\nRESPONSE:")
        while True:
            new = s.recv(4096)
            if not new:
                break
            print(f"{new}")
            # print(new)
